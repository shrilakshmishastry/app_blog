from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder = 'templates')

db = SQLAlchemy(app)

db.init_app(app)

from app import models


@app.route("/" , methods = ['GET' ])

def data():
    return render_template('home.html')
