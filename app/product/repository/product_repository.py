from app.product.model.entity.product import Product
from sqlalchemy.exc import SQLAlchemyError

class ProductRepository:
    def __init__(self, session):
        self.session = session

    def find_all(self):
        return self.session.query(Product).all()
    
    def save(self, product: Product):
        try:
            self.session.add(product)
            self.session.commit()
            return product
        except SQLAlchemyError as e:
            self.session.rollback()
            raise RuntimeError("Problem z zapisaniem w bazie danych") from e