from flask import Blueprint, request, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from utils.user_data_handler import save_user_data
import os

auth_bp = Blueprint('auth', __name__)
CORS(auth_bp)
bcrypt = Bcrypt()

@auth_bp.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    hashed_password = bcrypt.generate_password_hash(password, 10).decode('utf-8')

    user_data = {
        'email': email,
        'password': hashed_password
    }

    db_path = os.path.join(os.getcwd(), 'users.json')

    save_user_data(db_path, user_data)

    return jsonify({"message": "User saved"}), 201


@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')


@auth_bp.route('/api/logout', methods=['GET'])
def logout():
    pass
