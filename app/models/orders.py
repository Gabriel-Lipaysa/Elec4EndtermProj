from app import db
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP, DECIMAL
from sqlalchemy.orm.relationships import Relationship
from datetime import datetime

class Orders(db.Model):
    __tablename__ = 'orders'

    id = Column(BIGINT(unsigned=True), primary_key=True)
    user_id = Column(BIGINT(unsigned=True), ForeignKey('users.id', ondelete='CASCADE'), unique=True,  nullable=False)
    total_price = Column(DECIMAL(10,2), nullable=False)
    status = Column(String(255), nullable = False, server_default='pending')
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())

    user = Relationship('User', backref='orders', lazy=True)