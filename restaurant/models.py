# this is an application that is used to create the database with two tables for users and the resouces
from datetime import datetime

from flask_login import UserMixin

from restaurant import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Used to create a table for the users
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    type = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    offers = db.relationship('Offers', backref='customer', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.type}' )" # Returns the required data from the database without the passord


# To be used to create a table for offers available
class Offers(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key=True)
    offer_name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    offer_type = db.Column(db.String(20), nullable=False)
    price = db.Column(db.String(10), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    book_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Offers('{self.offer_name}','{self.description}','{self.status}' ,'{self.offer_type}' ,'{self.price}')" # Returns the required data from the database

