#!/usr/bin/python3
"""
Flask API with Basic Auth, JWT Auth and Role-Based Access COntrol
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "12345678"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users storage
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"}
}

# =======================
# BASIC AUTHENTICATION
# =======================

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user.get("password"), password):
        return username
    return None

@auth.error_handler
def auth_error(status):
    return jsonify({"error": "Unauthorized access"}), 401

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


# =======================
# JWT AUTHENTICATION
# =======================

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing credentials"}), 401

    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(
            users[username]["password"], password
    ):
        additional_claims = {"role": users[username]["role"]}
        access_token = create_access_token(
            identity=username,
            additional_claims=additional_claims
        )
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"}), 200


# ===========================
# ROLE-BASED ACCESS CONTROL
# ===========================

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({"message": "Admin Access: Granted"}), 200


# ================================
# JWT ERROR HANDLERS (ALL 401)
# ================================

@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_fresh_token_required(err):
    return jsonify({"error": "Fresh token required"}), 401



if __name__ == "__main__":
    app.run()
