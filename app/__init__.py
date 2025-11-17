from flask import Flask
from app.database import db
from app.product.repository.product_repository import ProductRepository
from app.product.service.product_service import ProductService
from app.product.controller.product_controller import ProductController

class AppFactory:
    def __init__(self):
        self.app = Flask(__name__)
        self.configure_app()
        self.init_extensions()
        self.build_dependencies()
        self.register_controllers()
        self.create_database()

    def configure_app(self):
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    def init_extensions(self):
        db.init_app(self.app)

    def build_dependencies(self):
        self.product_repository = ProductRepository(db.session)
        self.product_service = ProductService(self.product_repository)
        self.product_controller = ProductController(self.product_service)

    def register_controllers(self):
        self.app.register_blueprint(self.product_controller.blueprint, url_prefix="/products")

    def create_database(self):
        with self.app.app_context():
            db.create_all()

    def get_app(self):
        return self.app
