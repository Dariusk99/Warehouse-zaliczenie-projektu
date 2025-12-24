from app.order.order import Order, OrderItem
from app.order.order_service import OrderService
from app.product.core.product_service import ProductService

class OrderAppService:
    def __init__(self, order_service: OrderService, product_service: ProductService):
        self.order_service = order_service
        self.product_service = product_service

    def create_order(self, order_data):
        order = Order(
            customer=order_data["customer"],
            address=order_data["address"],
            phone_number=order_data["phone_number"]
        )
        
        for item in order_data["products"]:
            product = self.product_service.get_by_id(item["product_id"])
            if not product:
                raise ValueError(f"Produkt o id {item['product_id']} nie istnieje")
            
            order_item = OrderItem(product=product, quantity=item["quantity"])
            order.items.append(order_item)
        
        self.order_service.save(order)
        return order