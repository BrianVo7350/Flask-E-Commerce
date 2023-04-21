from .auth_forms import SignUpForm, LogInForm
# from app.models import User
from flask import Blueprint, flash, redirect, render_template, request, url_for
# from flask_login import current_user, login_required, login_user, logout_user

auth = Blueprint('auth',__name__,template_folder='auth_templates')

@auth.route('/signup',methods=['GET','POST'])
def signupPage():
    form = SignUpForm()
    if request.method == 'GET':
        return render_template('signup.html',form=form)
    
    if not form.validate():
        flash("Sorry, what you  typed in was not valid, please try again","danger")
        return render_template('signup.html',form=form)
    
    email = form.email.data
    first_name = form.first_name.data
    last_name = form.last_name.data
    password = form.password.data

    print(email,first_name,last_name,password)
    
    return render_template('signup.html',form=form)


@auth.route('/login',methods=['GET','POST'])
def loginPage():
    form = LogInForm()
    if request.method == 'GET':
        return render_template('login.html',form=form)
    
    if not form.validate():
        flash("Sorry, what you typed in was not valid, please try again","danger")
        return render_template('login.html',form=form)
    
    print(form.email)
    
    return render_template('login.html',form=form)