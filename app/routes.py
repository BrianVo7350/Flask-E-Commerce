from app import app
from flask import url_for
from flask import flash, redirect, render_template, request, url_for
# from flask_login import current_user, login_required


@app.route('/')
def homePage():
    return render_template('index.html')
