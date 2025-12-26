from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required

class AuthController:
    def __init__(self, auth_service):
        self.auth_service = auth_service
        self.blueprint = Blueprint("auth", __name__)

        self.blueprint.add_url_rule("/register", "register", self.register, methods=["POST"])
        self.blueprint.add_url_rule("/login", "login", self.login, methods=["POST"])
        self.blueprint.add_url_rule("/logout", "logout", self.logout, methods=["POST"])

    def register(self):
        data = request.get_json()
        user = self.auth_service.register(
            data["username"], data["password"]
        )

        if not user:
            return jsonify({"error": "User istnieje"}), 400

        return jsonify({"message": "User został zarejestrowany"}), 201

    def login(self):
        data = request.get_json()
        user = self.auth_service.authenticate(
            data["username"], data["password"]
        )

        if not user:
            return jsonify({"error": "Nieprawidłowe dane"}), 401

        login_user(user)
        return jsonify({"message": "Zalogowano"}), 200

    @login_required
    def logout(self):
        logout_user()
        return jsonify({"message": "Wylogowano"})
