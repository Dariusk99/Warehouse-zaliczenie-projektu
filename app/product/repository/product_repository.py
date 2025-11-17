from app.product.model.entity.product import Product

class ProductRepository:
    def __init__(self, session):
        self.session = session

    def find_all(self):
        return self.session.query(Product).all()