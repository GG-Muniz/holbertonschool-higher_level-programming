#!/usr/bin/env python3
"""
A simple Flask API demonstratic CRUD operations
manages user data stored in memory - provides endpoints
for retrieveing, listing and adding users.
"""

from flask import Flask, jsonify, request

# Flask initialization
app = Flask(__name__)

# User data in memory
users = {}


@app.route('/')
def home():
    """
    Home/root endpoint - welcomes users to API.
    Returns:
        str: Welcome message
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_all_usernames():
    """
    Get all username endpoints
    Returns:
        JSON: list of all usernames in the system(memory)
    """
    usernames_list = list(users.keys())
    return jsonify(usernames_list)


@app.route('/status')
def status():
    """"
    Health check endpoint - verify API is running
    Returns:
        str: Status Message
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Retrieve a specific user by username
    Args:
        username (str): username to look up from URL
    Returns:
        JSON: complete user object - if found
        JSON: error message 404 status - if not found.
    """
    if username in users:
        return jsonify(users[username])
    else:
        error_response = {"error": "User not found"}
        return jsonify(error_response), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user to the system

    Expect JSON payload:
        - username: unique identifier
        - name: user's full name
        - age: user's age
        - city: user's location
    Returns:
        JSON: confirmation message with user data added.
    """
    data = request.get_json()

    if not data:
        error_response = {"error": "No data provided"}
        return jsonify(error_response), 400

    if 'username' not in data:
        error_response = {"error": "Username is required"}
        return jsonify(error_response), 400

    username = data['username']

    user_object = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }

    users[username] = user_object

    success_response = {
        "message": "User added",
        "user": user_object
    }

    return jsonify(success_response), 201


@app.errorhandler(404)
def not_found(error):
    """
    Global 404 error handler.
    Ensures 404 errors return JSON not HTML
    Args:
        error: error object from Flask
    Returns:
        JSON: error message 404 status
    """
    error_response = {"error": "Endpoint not found"}
    return jsonify(error_response), 404


if __name__ == '__main__':
    app.run(debug=False)
