from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User

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

    # cant get this to work right now,
    # tried passing current user but got an error
    # def validate_email(self, email):
    #     if user_info.email != email.data:
    #         user = User.query.filter_by(email=email.data).first()
    #         if user is not None:
    #             raise ValidationError('Please use a different email address.')

class EditAddressForm(FlaskForm):
    name = StringField('Address Name', validators=[DataRequired()])
    address_one = StringField('Address Line 1', validators=[DataRequired()])
    address_two = StringField('Address Line 2')
    city = StringField('City', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[DataRequired()])
    submit = SubmitField('Save')

class ToppingForm(FlaskForm):
    submit = SubmitField('Add to Cart')