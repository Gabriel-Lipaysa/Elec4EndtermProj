from app import db
from sqlalchemy import Column, ForeignKey, Integer, func
from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP, DECIMAL
from sqlalchemy.orm import relationship

class OrderItem(db.Model):
    __tablename__ = 'order_items'

    id = Column(BIGINT(unsigned=True), primary_key=True)
    order_id = Column(BIGINT(unsigned=True), ForeignKey('orders.id', ondelete='CASCADE'), unique=True, nullable=False)
    product_id = Column(BIGINT(unsigned=True), ForeignKey('products.id', ondelete='CASCADE'), unique=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10,2), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), server_onupdate=func.now())

    order = relationship('Order', backref='order_items', lazy=True)
    product = relationship('Product', backref='order_items', lazy=True)