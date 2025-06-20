#!/usr/bin/env python3
"""
Flask API with security features like:
    Basic Authentication and JWT tokens
Multiple authentications and role-based access control
"""
import os
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from functools import wraps

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'dev-key')

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def varify_password(username, password):
    """
    verify User and Password - basic verification
    Args:
        username(str): user provided
        password(str): user provided

    Returns:
        str: Username if authentication successful, None otherwise
    """
    if username in users:
        if check_password_hash(users[username]['password'], password):
            return username
    return None


# JWT Error Handlers - ensures all auth. errors return 401
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle missing Authorization header.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid tokens.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """
    Handle expired tokens.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """
    Handle revoked tokens.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """
    Handle tokens that need to be refreshed.
    """
    return jsonify({"error": "Fresh token required"}), 401


def admin_required():
    """
    Checks if current user is admin level.
    Must be used after @jwt_required() decorator
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            if claims.get('role') != 'admin':
                return jsonify({"error": "Admin access required"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator


# Routes
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Enpoint protected by basic authentication
    Requires valid username and password.
    Returns:
        str: Success message - if authenticated.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Accepts username/password and returns JWT token
    Returns:
        JSON: if credentials are valid - access token.
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing credentials"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if username in users:
        user = users[username]
        if check_password_hash(user['password'], password):
            additional_claims = {"role": user['role']}
            access_token = create_access_token(
                identity=username,
                additional_claims=additional_claims
            )
            return jsonify({"access_token": access_token}), 200

        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Enpoint protected by JWT authentication.
    Requires valid JWT token in Authorization Header
    Returns:
        str: Sucess message if authenticated.
    """
    current_user = get_jwt_identity()
    return "JWT AUTH: Access Granted"


@app.route('/admin-only')
@jwt_required()
@admin_required()
def admin_only():
    """
    Endpoint requiring JWT authentication and admin role
    Returns:
        str: Success if authenticated and has admin role.
    """
    return "Admin Access: Granted"


@app.errorhandler(404)
def not_found(error):
    """
    Global 404 - ensuring JSON responds for all endpoints.
    """
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """
    Handles incorrect HTTP methods.
    """
    return jsonify({"error": "Method not allowed"}), 405


if __name__ == '__main__':
    """
    Runs Flask DEvelopment Server.
    """
    app.run(debug=False, host='0.0.0.0', port=5000)
