from app.database import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", back_populates="orders")
    items = db.relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        items_str = "\n".join([repr(item) for item in self.items])
        return (f"Order(id={getattr(self, 'id', None)}, "
                f"customer={self.customer}, address={self.address}, "
                f"phone_number={self.phone_number}, "
                f"user_id={getattr(self, 'user_id', None)})\nItems:\n{items_str}")

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    order = db.relationship("Order", back_populates="items")
    product = db.relationship("Product")
