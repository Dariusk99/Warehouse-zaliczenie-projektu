from app.order.order import Order
from sqlalchemy.exc import SQLAlchemyError

class OrderRepository:
    def __init__(self, session):
        self.session = session

    def find_all(self):
        return self.session.query(Order).all()

    def find_by_id(self, order_id):
        return self.session.get(Order, order_id)
    
    def save(self, order: Order):
        try:
            self.session.add(order)
            self.session.commit()
            return order
        except SQLAlchemyError as e:
            self.session.rollback()
            return None