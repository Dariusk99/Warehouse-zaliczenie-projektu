from flask import Blueprint, Response, request, jsonify
import json
from app.product.model.dto.product_dto import ProductDTO, ProductSaveDTO

class ProductController:
    def __init__(self, product_service):
        self.product_service = product_service

        self.product_dto = ProductDTO()
        self.products_dto = ProductDTO(many=True)
        self.product_save_dto = ProductSaveDTO()

        self.blueprint = Blueprint("v1/products", __name__)
        self.blueprint.add_url_rule("/", view_func=self.find_all, methods=["GET"])
        self.blueprint.add_url_rule("/", view_func=self.register_product, methods=["POST"])

    def find_all(self):
        products = self.products_dto.dump(self.product_service.find_all())
        return Response(
            json.dumps(products, ensure_ascii=False),
            mimetype="application/json; charset=utf-8"
        )
    
    def register_product(self):
        validated = self.product_save_dto.load(request.get_json())
        saved_product = self.product_service.save(validated)

        if not saved_product:
            return jsonify({"error": "Nie udało się zapisać do bazy danych"}), 400
        
        return self.product_dto.dump(saved_product), 201