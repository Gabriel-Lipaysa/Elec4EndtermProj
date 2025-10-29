from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from .forms import ClientLoginForm, ClientRegisterForm
from .models import ClientUser
from . import db, bcrypt

bp = Blueprint('client', __name__)

@bp.route('/')
def index():
    if session.get('client_id'):
        return redirect(url_for('client.home'))
    return redirect(url_for('client.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = ClientLoginForm()  # Create form object
    if request.method == 'POST' and form.validate_on_submit():
        user = ClientUser.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['client_id'] = user.id
            session['client_email'] = user.email
            flash('Logged in successfully!', 'success')
            return redirect(url_for('client.home'))
        flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)  # Pass form to template

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = ClientRegisterForm()  # Create form object
    if request.method == 'POST' and form.validate_on_submit():
        if ClientUser.query.filter_by(email=form.email.data).first():
            flash('Email already registered.', 'warning')
        else:
            hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            new_user = ClientUser(email=form.email.data, password=hashed)
            db.session.add(new_user)
            db.session.commit()
            flash('Registered successfully! Please log in.', 'success')
            return redirect(url_for('client.login'))
    return render_template('register.html', form=form)  # Pass form to template

@bp.route('/home')
def home():
    if not session.get('client_id'):
        flash('Please log in first.', 'info')
        return redirect(url_for('client.login'))
    return render_template('home.html')

@bp.route('/logout')
def logout():
    session.pop('client_id', None)
    session.pop('client_email', None)
    flash('Logged out.', 'info')
    return redirect(url_for('client.login'))
