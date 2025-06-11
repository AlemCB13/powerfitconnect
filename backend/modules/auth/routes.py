from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .services import register_user, authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Username and password are required"}), 400

    user, error = register_user(username, password)
    if error:
        return jsonify({"msg": error}), 400

    return jsonify({"msg": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user, error = authenticate_user(username, password)

    if not user:
        return jsonify({"message": "Invalid username or password"}), 401
    access_token = create_access_token(identity=user.id)
    return jsonify({'token': access_token}), 200