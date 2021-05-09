
from . import database
from flask_login import UserMixin

class User(database.Model, UserMixin):
    """
    This class represents users 
    """
    __tablename__ = 'user'
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(100), unique=True)
    password = database.Column(database.String(128))

    def __init__(self, email, password):
        self.email = email
        self.password = password

class Employee(database.Model):
    __tablename__ = 'employee'
    e_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String);
    nid = database.Column(database.Integer, unique=True)
    contact = database.Column(database.String(11), unique=True)
    department = database.Column(database.String)
    u_id = database.Column(database.Integer, database.ForeignKey('user.id'))

    def __init__(self, name, nid, contact, id):
        self.name = name
        self.nid = nid
        self.contact = contact
        self.u_id = id

class Salary(database.Model):
    __tablename__ = 'salary'

    s_id = database.Column(database.Integer, primary_key=True)
    amount = database.Column(database.Integer)
    e_id = database.Column(database.Integer, database.ForeignKey('employee.e_id'))

    def __init__(self, amount, e_id):
        self.amount = amount
        self.e_id = e_id
