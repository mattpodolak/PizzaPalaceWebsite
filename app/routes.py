from app import flapp, url_for, request
from app.forms import LoginForm, RegistrationForm, EditProfileForm, EditAddressForm, CustomizeForm, AddressesForm
from flask import render_template, flash, redirect
from app.menudata import menu_items
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Address
from app import db
from werkzeug.urls import url_parse
import app.util as util

@flapp.route('/')
@flapp.route('/index')
def index():
    return render_template('index.html', title='Home')

@flapp.route('/deals')
def deals():
    #import data from a class containing all relational data
    deal_items = menu_items['deals']
    return render_template('menu.html', title='Deals', items=deal_items, category='deals')

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
        user = User(username=form.username.data, first_name=form.first_name.data , last_name=form.last_name.data , email=form.email.data, phone=form.phone.data)
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
    addresses = user.addresses
    return render_template('user.html', user=user, addresses=addresses)

@flapp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username, current_user.email)
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        current_user.phone = form.phone.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
        form.phone.data = current_user.phone
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)

@flapp.route('/add_address', methods=['GET', 'POST'])
@login_required
def add_address():
    form = EditAddressForm()
    if form.validate_on_submit():
        address = Address(name=form.name.data, address_one=form.address_one.data , address_two=form.address_two.data , postal_code=form.postal_code.data, city=form.city.data, author=current_user)
        db.session.add(address)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('add_address'))
    return render_template('edit_address.html', title='Add an Address', form=form)

@flapp.route('/customize/<category>/<id>', methods=['GET', 'POST'])
def customize(category, id):
    custom_item, pizza_list, default_toppings, wings_list, pops_list, dips_list = util.find_item(category, id)
    addons = custom_item['addon'] #might need to remove value from this
    form = CustomizeForm(pizzas=pizza_list, wings=wings_list, pops=pops_list, dips=dips_list, defaultToppings=default_toppings)
    if form.validate_on_submit():
        flash('Submit form')
    elif request.method == 'GET':
        flash('Load form')
    return render_template('customize.html', title='Customize Menu Item',
                           form=form, item=custom_item)

@flapp.route('/test', methods=['GET', 'POST'])
def test():
    user_addresses = [{"name": 'Name 1'},
                    {"name": 'Name 2'}]
    form = AddressesForm(addresses=user_addresses)
    return render_template("test.html", form=form)