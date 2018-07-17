from datetime import datetime
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    #in db.relat... referenced by model class ie: Post
    #posts is not a db field, defined one the "one" side of one-to-many relation
    #backref defines name of field for the "many" objs
    #lazy defines database query for relationship
    addresses = db.relationship('Address', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
        
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    address_one = db.Column(db.String(140))
    address_two = db.Column(db.String(140))
    city = db.Column(db.String(140))
    postal_code = db.Column(db.String(140))

    #in db.Fore... reference user.id user is database table name, referencing the id from this table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Address {}>'.format(self.name)