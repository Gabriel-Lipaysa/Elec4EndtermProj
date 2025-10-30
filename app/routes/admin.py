from flask import render_template, session, redirect, flash, url_for, request
from app import app, db, bcrypt
from app.forms import AdminLoginForm
from app.models.user import User

# ------------------------------------------------------------
# ADMIN LOGIN (now located at /login/admin)
# ------------------------------------------------------------
@app.route('/login/admin', methods=['GET', 'POST'])
def show_admin_login():
    form = AdminLoginForm()

    # If already logged in as admin, skip login
    if session.get('role') == 'admin':
        return redirect(url_for('admin_dashboard'))

    # Handle POST request (form submission)
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Query admin user directly using SQLAlchemy
        admin = User.query.filter_by(username=username, role='admin').first()

        if admin and bcrypt.check_password_hash(admin.password, password):
            session['user_id'] = admin.id
            session['role'] = admin.role
            flash('Admin logged in successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid admin credentials. Please try again.', 'danger')
            return redirect(url_for('show_admin_login'))

    # GET request or invalid form → show the login page
    return render_template('auth/admin-login.html', form=form)


# ------------------------------------------------------------
# ADMIN LOGOUT
# ------------------------------------------------------------
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('show_admin_login'))


# ------------------------------------------------------------
# ADMIN DASHBOARD
# ------------------------------------------------------------
@app.route('/admin/dashboard')
def admin_dashboard():
    # Require login
    if not session.get('user_id'):
        flash('Please log in first.', 'warning')
        return redirect(url_for('show_admin_login'))

    # Restrict access to admins only
    if session.get('role') != 'admin':
        flash('Access denied. Admins only.', 'danger')
        return redirect(url_for('show_admin_login'))

    # Render dashboard
    return render_template('admin/dashboard.html')
