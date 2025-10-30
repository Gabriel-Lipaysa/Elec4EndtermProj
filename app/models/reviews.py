from app import db
from sqlalchemy import Column, ForeignKey, Integer, func
from sqlalchemy.dialects.mysql import TEXT, BIGINT, TIMESTAMP
from sqlalchemy.orm import relationship

class Review(db.Model):
    __tablename__ = 'reviews'

    id = Column(BIGINT(unsigned=True), primary_key=True)
    user_id = Column(BIGINT(unsigned=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(BIGINT(unsigned=True), ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(TEXT, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), server_onupdate=func.now())

    user = relationship('User', backref='reviews', lazy=True)
    user = relationship('Product', backref='reviews', lazy=True)