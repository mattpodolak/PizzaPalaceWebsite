from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField, FormField, FieldList, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User
from app.toppings import WingsArray

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Save')

    def __init__(self, original_username, original_email, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email

    # incase i add username changing functionality later
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        if email.data != self.original_email:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError('Please use a different email address.')

class EditAddressForm(FlaskForm):
    name = StringField('Address Name', validators=[DataRequired()])
    address_one = StringField('Address Line 1', validators=[DataRequired()])
    address_two = StringField('Address Line 2')
    city = StringField('City', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[DataRequired()])
    submit = SubmitField('Save')

class PopForm(FlaskForm):
    pop = StringField('Pick a Pop')

class DipForm(FlaskForm):
    dip = StringField('Pick a Dip')

class PizzaForm(FlaskForm):
    pizza = StringField('Pick Pizza Toppings')

class CustomizeForm(FlaskForm):
    notes = StringField('Special Notes')
    submit = SubmitField('Add to Cart')

class AddressEntryForm(FlaskForm):
    #name = SelectField(choices=[('1', 'Potato'), ('2', 'Onion'), ('3', 'Tomato')])
    name = SelectField(choices=WingsArray)

class AddressesForm(FlaskForm):
    """A form for one or more addresses"""
    addresses = FieldList(FormField(AddressEntryForm), min_entries=1)
    submit = SubmitField('Save')