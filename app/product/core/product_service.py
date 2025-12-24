from app.product.core.product_repository import ProductRepository
from app.product.core.product_factory import create_product_from_dict

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def find_all(self):
        return self.product_repository.find_all()
    
    def get_by_id(self, product_id):
        return self.product_repository.find_by_id(product_id)
    
    def save(self, data):
        product = create_product_from_dict(data)
        saved_product = self.product_repository.save(product)

        if not saved_product:
            return None
        
        return saved_product