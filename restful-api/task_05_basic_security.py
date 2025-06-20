#!/usr/bin/env python3
"""
Flask API with JWT debugging to help identify authentication issues.
This version includes extensive logging to trace token creation and validation.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt, decode_token
)
from functools import wraps
import logging
from datetime import datetime, timedelta

# Set up logging to see what's happening
logging.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# JWT Configuration - with explicit settings
app.config['JWT_SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)  # Token valid for 24 hours
app.config['JWT_ALGORITHM'] = 'HS256'  # Explicitly set algorithm

# Initialize authentication handlers
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User database
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

logger.info("Application initialized with users: %s", list(users.keys()))


# ==================== BASIC AUTHENTICATION ====================

@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic authentication."""
    logger.debug("Basic auth attempt for username: %s", username)

    if username in users:
        user = users[username]
        if check_password_hash(user['password'], password):
            logger.info("Basic auth successful for user: %s", username)
            return username

    logger.warning("Basic auth failed for username: %s", username)
    return None


# ==================== JWT ERROR HANDLERS ====================

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing Authorization header."""
    logger.error("JWT Error - Missing authorization header: %s", err)
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid tokens."""
    logger.error("JWT Error - Invalid token: %s", err)
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired tokens."""
    logger.error("JWT Error - Token expired. Payload: %s", jwt_payload)
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked tokens."""
    logger.error("JWT Error - Token revoked")
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle tokens that need to be refreshed."""
    logger.error("JWT Error - Fresh token required")
    return jsonify({"error": "Fresh token required"}), 401


# ==================== ROLE-BASED ACCESS CONTROL ====================

def admin_required():
    """Decorator to check if the current user has admin role."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # Get JWT claims
            claims = get_jwt()
            current_user = get_jwt_identity()

            logger.debug("Admin check for user: %s with claims: %s", current_user, claims)

            # Check if user has admin role
            if claims.get('role') != 'admin':
                logger.warning("Admin access denied for user: %s (role: %s)",
                             current_user, claims.get('role'))
                return jsonify({"error": "Admin access required"}), 403

            logger.info("Admin access granted for user: %s", current_user)
            return fn(*args, **kwargs)
        return wrapper
    return decorator


# ==================== API ENDPOINTS ====================

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Endpoint protected by basic authentication."""
    logger.info("Basic protected endpoint accessed successfully")
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Login endpoint to obtain JWT token."""
    logger.debug("Login attempt received")

    # Get JSON data from request
    data = request.get_json()
    logger.debug("Login data received: %s", {k: v for k, v in (data or {}).items() if k != 'password'})

    # Validate request has data
    if not data:
        logger.warning("Login failed - no data provided")
        return jsonify({"error": "Missing credentials"}), 400

    # Extract credentials
    username = data.get('username')
    password = data.get('password')

    # Validate both fields are present
    if not username or not password:
        logger.warning("Login failed - missing username or password")
        return jsonify({"error": "Username and password required"}), 400

    # Check if user exists and password is correct
    if username in users:
        user = users[username]
        if check_password_hash(user['password'], password):
            # Create JWT token with user identity and role
            additional_claims = {"role": user['role']}

            # Create the token
            access_token = create_access_token(
                identity=username,
                additional_claims=additional_claims
            )

            # Log token creation for debugging
            logger.info("JWT token created for user: %s with role: %s", username, user['role'])

            # Decode token to verify it was created correctly (for debugging)
            try:
                decoded = decode_token(access_token)
                logger.debug("Token decoded successfully. Identity: %s, Claims: %s",
                           decoded.get('sub'), decoded.get('role'))
            except Exception as e:
                logger.error("Failed to decode created token: %s", e)

            return jsonify({"access_token": access_token}), 200

    # Invalid credentials
    logger.warning("Login failed - invalid credentials for username: %s", username)
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Endpoint protected by JWT authentication."""
    # Get the username from the JWT token
    current_user = get_jwt_identity()
    claims = get_jwt()

    logger.info("JWT protected endpoint accessed by user: %s with claims: %s",
               current_user, claims)

    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
@admin_required()
def admin_only():
    """Endpoint requiring both JWT authentication and admin role."""
    current_user = get_jwt_identity()
    logger.info("Admin endpoint accessed successfully by: %s", current_user)
    return "Admin Access: Granted"


# ==================== DEBUG ENDPOINT ====================

@app.route('/debug/verify-token', methods=['POST'])
def debug_verify_token():
    """
    Debug endpoint to verify what's in a JWT token.
    Send the token in the request body to see its contents.
    """
    data = request.get_json()
    token = data.get('token')

    if not token:
        return jsonify({"error": "No token provided"}), 400

    try:
        # Decode the token without verification (for debugging only!)
        import jwt as pyjwt
        decoded = pyjwt.decode(token, options={"verify_signature": False})

        # Also try to decode with verification
        try:
            verified_decoded = decode_token(token)
            verified = True
        except Exception as e:
            verified = False
            verified_decoded = str(e)

        return jsonify({
            "token_contents": decoded,
            "signature_verified": verified,
            "verification_result": verified_decoded if not verified else "Token is valid"
        })
    except Exception as e:
        return jsonify({"error": f"Failed to decode token: {str(e)}"}), 400


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors with JSON response."""
    logger.warning("404 error - endpoint not found")
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors with JSON response."""
    logger.warning("405 error - method not allowed")
    return jsonify({"error": "Method not allowed"}), 405


# ==================== STARTUP INFO ====================

@app.before_first_request
def startup_info():
    """Log startup information."""
    logger.info("=" * 60)
    logger.info("Flask JWT Debug Server Started")
    logger.info("JWT Secret Key Length: %d", len(app.config['JWT_SECRET_KEY']))
    logger.info("JWT Algorithm: %s", app.config['JWT_ALGORITHM'])
    logger.info("Token Expiration: %s", app.config['JWT_ACCESS_TOKEN_EXPIRES'])
    logger.info("=" * 60)


if __name__ == '__main__':
    """Run Flask development server with debugging enabled."""
    logger.info("Starting Flask application...")
    app.run(debug=True, host='0.0.0.0', port=5000)
