from app.order.order_repository import OrderRepository
from app.order.order import Order

class OrderService:
    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def find_all(self):
        return self.order_repository.find_all()
    
    def find_by_id(self, order_id):
        return self.order_repository.find_by_id(order_id)
    
    def save(self, order: Order):
        saved_order =  self.order_repository.save(order)

        if not saved_order:
            return None
        
        return saved_order