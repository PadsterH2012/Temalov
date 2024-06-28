from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import RegistrationForm, LoginForm
from app.models import Player
from app import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.welcome'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        player = Player(username=form.username.data, password=hashed_password)
        db.session.add(player)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.welcome'))
    form = LoginForm()
    if form.validate_on_submit():
        player = Player.query.filter_by(username=form.username.data).first()
        if player and bcrypt.check_password_hash(player.password, form.password.data):
            login_user(player)
            return redirect(url_for('main.welcome'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
