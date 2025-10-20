from app import db
from datetime import datetime
from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP

# class User(db.Model):
#     __tablename__='users'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     username = db.Column(db.String(255),nullable=False)
#     email = db.Column(db.String(255), unique=True, nullable=True)
#     password = db.Column(db.String(255), nullable=False)
#     role = db.Column(db.Enum('admin', 'user'), name='role', default='user')
#     created_at = db.Column(db.DateTime, default=datetime.now())
#     updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())


class User(db.Model):
    __tablename__='users'

    id = Column(BIGINT(unsigned=True), primary_key=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), unique=True,nullable=False)
    email = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    role = Column(Enum('admin', 'user'), name='role', server_default='user')
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())