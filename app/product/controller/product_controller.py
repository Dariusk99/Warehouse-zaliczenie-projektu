from flask import Blueprint, Response
import json
from app.product.model.dto.product_dto import ProductDTO

class ProductController:
    def __init__(self, product_service):
        self.product_service = product_service

        self.products_dto = ProductDTO(many=True)

        self.blueprint = Blueprint("products", __name__)
        self.blueprint.add_url_rule("/", view_func=self.find_all, methods=["GET"])

    def find_all(self):
        products = self.products_dto.dump(self.product_service.find_all())
        return Response(
            json.dumps(products, ensure_ascii=False),
            mimetype="application/json; charset=utf-8"
        )
