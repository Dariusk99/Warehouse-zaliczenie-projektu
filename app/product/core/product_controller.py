from flask import Blueprint, Response, request, jsonify
import json
from app.product.core.product_dto import ProductDTO, ProductSaveDTO

class ProductController:
    def __init__(self, product_service):
        self.product_service = product_service

        self.product_dto = ProductDTO()
        self.products_dto = ProductDTO(many=True)
        self.product_save_dto = ProductSaveDTO()

        self.blueprint = Blueprint("v1/products", __name__)
        self.blueprint.add_url_rule("/", view_func=self.find_all, methods=["GET"])
        self.blueprint.add_url_rule("/", view_func=self.register_product, methods=["POST"])
        self.blueprint.add_url_rule("/<int:product_id>", "get_product", self.get_product, methods=["GET"])
        self.blueprint.add_url_rule("/<int:product_id>/<int:new_quantity>", "update_quantity", self.update_quantity, methods=["PUT"])

    def find_all(self):
        products = self.products_dto.dump(self.product_service.find_all())
        return Response(
            json.dumps(products, ensure_ascii=False),
            mimetype="application/json; charset=utf-8"
        )
    
    def register_product(self):
        validated = self.product_save_dto.load(request.get_json())
        print(validated)
        saved_product = self.product_service.save(validated)

        if not saved_product:
            return jsonify({"error": "Nie udało się zapisać do bazy danych"}), 400
        
        return self.product_dto.dump(saved_product), 201
    
    def get_product(self, product_id):
        product = self.product_service.get_by_id(product_id)
        if not product:
            return jsonify({"error": "Nie znaleziono produktu"}), 404
        return self.product_dto.dump(product), 201
    
    def update_quantity(self, product_id, new_quantity):
        updated_product = self.product_service.update_quantity(product_id, new_quantity)
        if not updated_product:
            return jsonify({"error": "Nie udało się zaktualizować produktu"}), 400

        return self.product_dto.dump(updated_product), 200