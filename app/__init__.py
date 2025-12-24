from flask import Flask, render_template
from app.database import db
from app.product.core.product_repository import ProductRepository
from app.product.core.product_service import ProductService
from app.product.core.product_controller import ProductController
from app.order.order_repository import OrderRepository
from app.order.order_service import OrderService
from app.order.order_app_service import OrderAppService
from app.order.order_controller import OrderController

class AppFactory:
    def __init__(self):
        self.app = Flask(__name__)
        self.configure_app()
        self.init_extensions()
        self.build_dependencies()
        self.register_controllers()
        self.register_routes()
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

        self.order_repository = OrderRepository(db.session)
        self.order_service = OrderService(self.order_repository)
        self.order_app_service = OrderAppService(self.order_service, self.product_service)
        self.order_controller = OrderController(self.order_service, self.order_app_service)

    def register_controllers(self):
        self.app.register_blueprint(self.product_controller.blueprint, url_prefix="/v1/products")
        self.app.register_blueprint(self.order_controller.blueprint, url_prefix="/v1/orders")

    def register_routes(self):
        @self.app.get("/")
        def index():
            return render_template("index.html")
        
        @self.app.get("/shop")
        def shop():
            return render_template("shop.html")
        
        @self.app.get("/warehouse")
        def warehouse():
            return render_template("warehouse.html")
        
        @self.app.get("/orders")
        def orders():
            return render_template("orders.html")

    def create_database(self):
        with self.app.app_context():
            db.create_all()

    def get_app(self):
        return self.app
