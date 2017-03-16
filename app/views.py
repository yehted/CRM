from flask import render_template
from flask_login import login_requred

from app import app

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/dashboard')
@login_requred
def dashboard():
    return render_template("about.html")
