from app.product.repository.product_repository import ProductRepository
from app.product.model.entity.product import Product

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def find_all(self):
        return self.product_repository.find_all()
    
    def save(self, data):
        product = Product(**data)
        saved_product = self.product_repository.save(product)

        if not saved_product:
            return None
        
        return saved_product