from flask import render_template  # pre-code for Flask webapps
from app import app, shopping_list


@app.route('/')  # how Flask specifies webpages
def index():
    return render_template('index.html', msg='Hello world')


@app.route('/grocery')  # shopping list page
def grocery():
    return render_template('grocery.html', shopping_list=shopping_list)
