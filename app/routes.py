from app import flapp, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask import render_template, flash, redirect
from app.menudata import menu_items
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app import db
from werkzeug.urls import url_parse

@flapp.route('/')
@flapp.route('/index')
def index():
    return render_template('index.html', title='Home')

@flapp.route('/deals')
def deals():
    #import data from a class containing all relational data
    deal_items = menu_items['deals']
    return render_template('menu.html', title='Deals', items=deal_items)

@flapp.route('/sides')
def sides():
    return render_template('menu.html', title='Sides')

@flapp.route('/specialtypizza')
def specialtypizza():
    return render_template('menu.html', title='Specialty Pizza')

@flapp.route('/sandwiches')
def sandwiches():
    return render_template('menu.html', title='Sandwiches')

@flapp.route('/wings')
def wings():
    return render_template('menu.html', title='Wings')

@flapp.route('/cart')
def cart():
    return render_template('cart.html', title='Cart')

@flapp.route('/checkout')
def checkout():
    return render_template('checkout.html', title='Checkout')

@flapp.route('/login', methods=['GET', 'POST'])
def login():
    # check if logged in currently
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@flapp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@flapp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@flapp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    addresses = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)