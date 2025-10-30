from flask import render_template, session, redirect, flash, url_for, request
from app import app, db, bcrypt
from app.models.user import User
from app.forms import UserLoginForm, UserRegisterForm


# ------------------------------------------------------------
# USER LOGIN
# ------------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def show_user_login():
    form = UserLoginForm()

    # If user is already logged in
    if session.get('role') == 'user':
        return redirect(url_for('user_dashboard'))

    # Validate login form
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email, role='user').first()

        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['role'] = user.role
            flash('User logged in successfully!', 'success')
            return redirect(url_for('user_dashboard'))
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('auth/user-login.html', form=form)


# ------------------------------------------------------------
# USER REGISTRATION
# ------------------------------------------------------------
@app.route('/signup', methods=['GET', 'POST'])
def show_user_signup():
    form = UserRegisterForm()

    # Redirect logged-in users away
    if session.get('role') == 'user':
        return redirect(url_for('user_dashboard'))

    if request.method == 'POST' and form.validate_on_submit():
        # Get form inputs
        name = request.form.get('name')
        username = request.form.get('username')
        email = form.email.data
        password = form.password.data
        confirm_password = request.form.get('confirm_password')

        # Validate password match
        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('show_user_signup'))

        # Check for duplicates
        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()
        if existing_user:
            flash('Username or email already exists.', 'warning')
            return redirect(url_for('show_user_signup'))

        # Hash password
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create new user record
        new_user = User(
            name=name,
            username=username,
            email=email,
            password=hashed_pw,
            role='user'
        )

        # Commit to database
        db.session.add(new_user)
        db.session.commit()

        # Auto-login after registration
        session['user_id'] = new_user.id
        session['role'] = 'user'

        flash('Registration successful! Welcome to Wagging Wonders.', 'success')
        return redirect(url_for('user_dashboard'))

    return render_template('auth/user-signup.html', form=form)


# ------------------------------------------------------------
# USER LOGOUT
# ------------------------------------------------------------
@app.route('/user/logout')
def user_logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('show_user_login'))


# ------------------------------------------------------------
# USER DASHBOARD
# ------------------------------------------------------------
@app.route('/user/dashboard')
def user_dashboard():
    if not session.get('user_id'):
        flash('Please log in first.', 'warning')
        return redirect(url_for('show_user_login'))

    if session.get('role') != 'user':
        flash('Access denied. Users only.', 'danger')
        return redirect(url_for('show_user_login'))

    return render_template('user/dashboard.html')
