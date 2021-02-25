from flask import render_template, request  # pre-code for Flask webapps
from app import app, shopping_list
from app.forms import NewItemForm


@app.route('/')  # how Flask specifies webpages
def index():
    return render_template('index.html', msg='Hello world')


@app.route('/grocery', methods=['GET', 'POST'])  # shopping list page
def grocery():
    form = NewItemForm()  # form we made
    if form.validate_on_submit():  # runs for POST requests from new item form
        shopping_list.append(
            {
                'name': request.form['name'],
                'quantity': request.form['quantity']
            })
    return render_template('grocery.html', form=form,
                           shopping_list=shopping_list)
