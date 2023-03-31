# The module is used for data submission of the web forms; registration, login, and adding offers

from flask_wtf import FlaskForm  # used in rendering forms for web applications
from wtforms import BooleanField  # importing data types of the string fields
from wtforms import (DateField, PasswordField, SelectField, StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import (  # validations for entry values enterded in the forms
    DataRequired, Email, EqualTo, Length, ValidationError)

from restaurant.models import Offers, User

user = [('User'), ('Admin'),('Employee')]
# the registration forms provided when registering the users
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    type = SelectField('Type of user', choices=user, validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # The function ensures that there is no existing similar user name
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('User name already exists')
    # The function ensures that there is no existing similar email
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('A user exist with a similar email')

# The login form for already registered users
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_password = BooleanField('Remember me')
    submit = SubmitField('Log in')

# Form used for adding offers
offers_available = [("Room"), ("Dish"), ("Conference room"), ("Sport")]
class OfferForm(FlaskForm):
    offer_name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    offer_type = SelectField('offer_type', choices=offers_available, validators=[DataRequired()])
    submit = SubmitField('Add')

class Booking(FlaskForm):
    book_date = DateField('book_date', format='%Y-%m-%d') 
    submit = SubmitField('Book now')