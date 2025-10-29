from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    # Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/elec4_endterm'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'SECRET_KEY'

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    bcrypt.init_app(app)

    # Import and register blueprint
    from .routes import bp as client_bp
    app.register_blueprint(client_bp)  # No prefix, routes are /login, /register, etc.

    return app
