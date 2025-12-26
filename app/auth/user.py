from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from app.database import db

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
