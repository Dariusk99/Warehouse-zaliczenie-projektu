from app.database import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    items = db.relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    order = db.relationship("Order", back_populates="items")
    product = db.relationship("Product")
