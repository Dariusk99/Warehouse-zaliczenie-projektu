from app.product.core.product import Product
from app.product.manufactured.manufactured import Manufactured

def create_product_from_dict(data: dict):
    product_type = data.get("product_type", "product")

    type_map = {
        "product": Product,
        "manufactured": Manufactured
    }

    model_cls = type_map.get(product_type)
    if not model_cls:
        raise ValueError(f"Unsupported product_type: {product_type}")

    return model_cls(**data)