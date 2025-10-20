from flask import render_template, session, redirect, flash, url_for
from app import app
from app.forms import AdminLoginForm
from app.controllers.auth_controller import authenticate_user

@app.route('/admin', methods=['GET','POST'])
def show_admin_login():
    form = AdminLoginForm()
    
    if session.get('role') == 'admin':

        return redirect(url_for('admin_dashboard'))
    
    if form.validate_on_submit():
        username = form.username.data  
        password = form.password.data  

        user = authenticate_user(username, password)

        if user and user.role == 'admin':
            session['user_id'] = user.id
            session['role'] = user.role
            flash('Admin logged in successfully!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials.', 'danger')
            return redirect(url_for('show_admin_login'))
    else:
        if form.errors:
            print('Form Errors:', form.errors)

    return render_template('auth/admin-login.html',form=form)

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('show_admin_login'))

@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('user_id'):
        flash('Please log in first.', 'warning')
        return redirect(url_for('show_admin_login'))
    if session.get('role') != 'admin':
        flash('Access denied. Admins only.', 'danger')
        return redirect(url_for('show_admin_login'))
    
    return render_template('admin/dashboard.html')

