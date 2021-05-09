from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from ..models import Employee
from ..models import AccountOfficer
from ..models import Manager

from .. import database

views = Blueprint('views', __name__)


@views.route('/stuffs')
@login_required
def stuff():
    """
    This method is used for stuff function and it collects 3 different types of data from 3 table employee, manager & acountofficer then render data. This function has done query & save data. 
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns stuff details page which is a HTML page. 
    :rtype: HttpResponse.
    """
    employees = Employee.query.all()
    managers = Manager.query.all()
    account_officers = AccountOfficer.query.all()

    return render_template("stuff.html", user=current_user, employees=employees, managers=managers, account_officers=account_officers)

@views.route('/')
@login_required
def home():
    """
    This method is used to display Home page. It's a HTML page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a home page which is a HTML page. 
    :rtype: HttpResponse.
    """
    return render_template("home.html", user=current_user)