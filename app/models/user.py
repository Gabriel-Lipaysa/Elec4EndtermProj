from app import db
from datetime import datetime
from sqlalchemy import Column, String, Enum, func
from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP

class User(db.Model):
    __tablename__ = 'users'

    id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum('admin', 'user', name='role_enum'), server_default='user', nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
