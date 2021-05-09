from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from .. import database
from ..models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    This method takes data from the form & authenticates by checking what kind of http request method. This method used to login.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a login page which is a HTML page. 
    :rtype: HttpResponse.
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in sucessfully', category='success')

                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
        """
    This method deletes the sesson that are create during the login. This method used to logout.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a login page which is a HTML page. 
    :rtype: HttpResponse.
    """
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
            """
    This method used to signup for new users.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a signup page which is a HTML page. 
    :rtype: HttpResponse.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()

        # validation
        if user:
            flash('Email exists!', category='error')
        elif len(password) < 6:
            flash('Password must be 6 character or more.', category='error')
        elif password != confirm_password:
            flash('Passwords don\'t match', category='error')
        else:
            # add user to database
            new_user = User(email=email, password=generate_password_hash(password, method='sha256'))
            database.session.add(new_user)
            database.session.commit()

            flash('Account created successfullty', category='success')
            return redirect(url_for('auth.login'))

    return render_template('signup.html', user=current_user)
