from app.database import db
from ..core.product import Product

class Manufactured(Product):
    __mapper_args__ = {
        "polymorphic_identity": "Produkt gotowy"
    }

    bom_id = db.Column(db.Integer)
    serial_number = db.Column(db.Integer)