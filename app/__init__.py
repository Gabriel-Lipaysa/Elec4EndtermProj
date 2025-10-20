from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@127.0.0.1/elec4_endterm'
app.secret_key='SECRET_KEY'

db = SQLAlchemy(app)
migrate = Migrate(app,db)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

from .models import user, products, carts, orders
from .routes import admin