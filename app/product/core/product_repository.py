from app.product.core.product import Product
from sqlalchemy.exc import SQLAlchemyError

class ProductRepository:
    def __init__(self, session):
        self.session = session

    def find_all(self):
        return self.session.query(Product).all()
    
    def find_by_id(self, product_id):
        return self.session.get(Product, product_id)
    
    def update_quantity(self, product_id, quantity):
        product = self.find_by_id(product_id)

        if not product:
            return None

        product.quantity = quantity
        self.session.commit()
        self.session.refresh(product)

        return product
    
    def find_by_index(self, index):
        return Product.query.filter_by(index=index).first()
    
    def save(self, product: Product):
        try:
            self.session.add(product)
            self.session.commit()
            return product
        except SQLAlchemyError as e:
            self.session.rollback()
            return None