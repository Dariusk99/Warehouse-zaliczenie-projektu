from app.database import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    location = db.Column(db.String(20))
    category = db.Column(db.String(20))