from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Instantiate the database
db = SQLAlchemy()

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),nullable = False,unique=True)
    password = db.Column(db.String,nullable=False)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50))
    date_joined = db.Column(db.DateTime,nullable = False, default=datetime.utcnow())

    def __init__(self, email, password, first_name,last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()