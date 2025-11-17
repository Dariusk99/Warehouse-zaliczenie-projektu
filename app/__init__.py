from flask import Flask
from app.database import db

class AppFactory:
    def __init__(self):
        self.app = Flask(__name__)
        self.configure_app()
        self.init_extensions()
        self.create_database()

    def configure_app(self):
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    def init_extensions(self):
        db.init_app(self.app)

    def create_database(self):
        with self.app.app_context():
            db.create_all()

    def get_app(self):
        return self.app
