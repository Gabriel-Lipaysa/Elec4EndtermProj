from app import db
from datetime import datetime
<<<<<<< HEAD
from sqlalchemy import Column, String, Enum, func
=======
from sqlalchemy import Column, String, Enum
>>>>>>> 4d8501a9645ae7334eb7498fbc11ac6038fc7078
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
<<<<<<< HEAD
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
=======
    __tablename__='users'

    id = Column(BIGINT(unsigned=True), primary_key=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), unique=True,nullable=False)
    email = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    role = Column(Enum('admin', 'user'), name='role', server_default='user')
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())
>>>>>>> 4d8501a9645ae7334eb7498fbc11ac6038fc7078
