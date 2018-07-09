from app import flapp
from app.forms import LoginForm
from flask import render_template, flash, redirect
import app.menudata

@flapp.route('/')
@flapp.route('/index')
def index():
    return render_template('index.html', title='Home')

@flapp.route('/deals')
def deals():
    #import data from a class containing all relational data
    deal_items = [
        {
            'name': 'Large Pizza Deal',
            'desc': 'Beautiful day in Portland!',
            'price': '15'
        },
        {
            'name': 'Large Pizza Deal',
            'desc': 'Beautiful day in Portland!',
            'price': '15'
        },
        {
            'name': 'Large Pizza Deal',
            'desc': 'Beautiful day in Portland!',
            'price': '15'
        }
    ]
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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
