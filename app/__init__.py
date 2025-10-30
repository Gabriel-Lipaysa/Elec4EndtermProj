from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

# ------------------------------------------------------------
# Flask App Configuration
# ------------------------------------------------------------
app = Flask(__name__)

# --- SECRET KEY (for sessions and CSRF protection) ---
app.config['SECRET_KEY'] = 'your-very-secure-secret-key'

# --- MySQL Database Connection ---
# Replace with your own credentials and DB name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@127.0.0.1/elec4_endterm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ------------------------------------------------------------
# Initialize Extensions
# ------------------------------------------------------------
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

# ------------------------------------------------------------
# Import Models (Order Matters)
# ------------------------------------------------------------
from app.models import user, products, carts, orders

# ------------------------------------------------------------
# Import Routes
# ------------------------------------------------------------
from app.routes import admin
from app.routes import user  # your user routes (auth, signup, etc.)

# ------------------------------------------------------------
# Default Route Redirect
# ------------------------------------------------------------
@app.route('/')
def default_redirect():
    return redirect(url_for('show_user_login'))
