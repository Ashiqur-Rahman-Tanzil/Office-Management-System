from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from ..models import Employee
from ..models import Salary

from .. import database

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    """ This method is used to display home page. It's gender a HTML page.
    
    :param request: it's a HttpResponse from user. 
    
    :type request: HttpResponse. 

    :return: this method returns a home page which is a HTML page. 
    
    :rtype: HttpResponse. 
    """
    return render_template("home.html", user=current_user)


@views.route('/salary')
@login_required
def account():
    """
    This method is used for called account function and  in database two table which
    is employee table and user table have e_id, this function has done query and save the data in a variable which name is account.

    :param request: it's a HttpResponse from user
    
    :type request: HttpResponse.

    :return: this method returns salary page when user wants to see their salary.

    :rtype: HttpResponse.
    """
    accounts = database.session.query(
        Employee, Salary
    ).filter(
        Employee.e_id == Salary.e_id
    ).all()

    # for account in accounts:
    #     print(account.Employee.name)

    print(accounts)
    return render_template("salary.html", user=current_user, accounts = accounts)
    
