from flask import Blueprint, Response, request, jsonify
import json
from app.order.order_dto import OrderDTO, OrderSaveDTO

class OrderController:
    def __init__(self, order_service, order_app_service):
        self.order_service = order_service
        self.order_app_service = order_app_service

        self.order_dto = OrderDTO()
        self.order_save_dto = OrderSaveDTO()
        self.orders_dto = OrderDTO(many=True)

        self.blueprint = Blueprint("orders", __name__)
        self.blueprint.add_url_rule("/", "find_all", self.find_all, methods=["GET"])
        self.blueprint.add_url_rule("/", "save_order", self.save_order, methods=["POST"])
        self.blueprint.add_url_rule("/<int:order_id>", "get_order", self.get_order, methods=["GET"])

    def find_all(self):
        orders = self.orders_dto.dump(self.order_service.find_all())
        return Response(
            json.dumps(orders, ensure_ascii=False),
            mimetype="application/json; charset=utf-8"
        )
    
    def get_order(self, order_id):
        order = self.order_service.find_by_id(order_id)
        if not order:
            return jsonify({"error": "Order not found"}), 404
        return self.order_dto.dump(order), 201

    def save_order(self):
        validated = self.order_save_dto.load(request.get_json())
        try:
            order = self.order_app_service.create_order(validated)
            return self.order_dto.dump(order), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
