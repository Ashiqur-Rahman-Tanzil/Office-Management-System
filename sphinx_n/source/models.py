from . import database
from flask_login import UserMixin


class User(database.Model, UserMixin):
    __tablename__ = 'user'
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(100), unique=True)
    password = database.Column(database.String(128))

    def __init__(self, email, password):
        self.email = email
        self.password = password
"""
    This class used to create Users for database entry
"""
class Employee(database.Model):
    __tablename__ = 'employee'
    e_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String);
    nid = database.Column(database.Integer, unique=True)
    contact = database.Column(database.String(11), unique=True)
    u_id = database.Column(database.Integer, database.ForeignKey('user.id'))

    def __init__(self, name, nid, contact, id):
        self.name = name
        self.nid = nid
        self.contact = contact
        self.u_id = id
"""
    This class used to create Employees for database entry
"""
class Manager(database.Model):
    __tablename__ = 'manager'
    m_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String);
    nid = database.Column(database.Integer, unique=True)
    contact = database.Column(database.String(11), unique=True)
    branch = database.Column(database.String)
    u_id = database.Column(database.Integer, database.ForeignKey('user.id'))

    def __init__(self, name, nid, contact, branch,  id):
        self.name = name
        self.nid = nid
        self.contact = contact
        self.u_id = id
        self.branch = branch
"""
    This class used to create Manager for database entry
"""
class AccountOfficer(database.Model):
    __tablename__ = 'acount_officer'
    ao_id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String);
    nid = database.Column(database.Integer, unique=True)
    contact = database.Column(database.String(11), unique=True)
    u_id = database.Column(database.Integer, database.ForeignKey('user.id'))

    def __init__(self, name, nid, contact, id):
        self.name = name
        self.nid = nid
        self.contact = contact
        self.u_id = id
"""
    This class used to create Accountofficers for database entry
"""
