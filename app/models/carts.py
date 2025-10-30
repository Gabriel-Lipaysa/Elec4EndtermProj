from app import db
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP 
from datetime import datetime

class Carts(db.Model):
    __tablename__ = 'carts'
    id = Column(BIGINT(unsigned=True), primary_key=True)
    user_id = Column(BIGINT(unsigned=True), nullable=False)
    product_id = Column(BIGINT(unsigned=True), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())