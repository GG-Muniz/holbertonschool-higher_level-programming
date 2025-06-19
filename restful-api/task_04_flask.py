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
def get_users():
    """
    Get all username endpoints
    Returns:
        JSON: list of all usernames in the system(memory)
    """
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def status():
    """"
    Health check endpoint - verify API is running
    Returns:
        str: Status Message
    """
    return "OK"


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
        return jsonify({"error": "No data provided"}), 400

    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']

    user_data = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }

    users[username] = user_data

    response = {
        "message": "User added",
        "user": user_data
    }
    return jsonify(response), 201


if __name__ == '__main__':
    app.run(debug=False)
