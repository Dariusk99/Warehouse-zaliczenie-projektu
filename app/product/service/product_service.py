from app.product.repository.product_repository import ProductRepository

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def find_all(self):
        return self.product_repository.find_all()