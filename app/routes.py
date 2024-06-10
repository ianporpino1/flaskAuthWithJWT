from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.services import UserService

def register_routes(app):
    @app.route('/users/', methods=['GET'])
    @jwt_required()
    def get_users():
        users = UserService.get_all_users()
        return jsonify([user.to_dict() for user in users])

    @app.route('/users/', methods=['POST'])
    def add_user():
        data = request.get_json()
        new_user = UserService.create_user(data['username'],data['password'], data['email'])
        return jsonify(new_user.to_dict()), 201

    from app.auth import register_auth_routes
    register_auth_routes(app)