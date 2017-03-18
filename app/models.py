from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

import enum

class Employee(UserMixin, db.Model):
    """ Employee table """

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """ Prevent password from being accessed """
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """ Set password to a hashed password """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """ Check if hashed password matches actual password """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class States(enum.Enum):
    IL = 'Illinois'
    WI = 'Wisconsin'
    MI = 'Michigan'
    IA = 'Iowa'
    MN = 'Minnesota'


class Customer(db.Model):
    """ Create a Customer table """

    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    street_address = db.Column(db.String(120))
    city = db.Column(db.String(60))
    state = db.Column(db.Enum(States))
    contacts = db.relationship('Contact', backref='company', lazy='dynamic')


class Contact(db.Model):
    """ Contacts a Customer table """

    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    email_address = db.Column(db.String(60))
    phone_number = db.Column(db.String(20))
    title = db.Column(db.String(60))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    # projects


class Department(db.Model):
    """ Create a Deaprtment table """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Role(db.Model):
    """ Create a Role table """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)
