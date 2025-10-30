from app import db
from datetime import datetime
from sqlalchemy import Column, String, Text, Numeric, Enum, Integer
from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP
class Products(db.Model):
    __tablename__ = 'products'

    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(255), nullable=False)
    # description = db.Column(db.Text(255), nullable=False)
    # price = db.Column(db.Numeric(8,2), nullable=False)
    # quantity = db.Column(db.Integer, nullable=False)
    # image = db.Column(db.String(255))
    # category = db.Column(db.Enum('Dog Food', 'Cat Food'), default=None, nullable=False)
    # created_at = db.Column(db.DateTime, default=datetime.now())
    # update_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    id = Column(BIGINT(unsigned=True), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Numeric(8,2), nullable=False)
    quantity = Column(Integer, nullable=False)
    image = Column(String(255))
    category = Column(Enum('Dog Food', 'Cat Food'), default=None, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())