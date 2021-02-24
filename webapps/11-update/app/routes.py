from flask import render_template, request, redirect, url_for
from app import app, shopping_list
from app.forms import NewItemForm, UpdateItemForm


@app.route('/')
def index():
    return render_template('index.html', msg='Hello world')


@app.route('/grocery', methods=['GET', 'POST'])
def grocery():
    form = NewItemForm()
    if form.validate_on_submit():
        shopping_list.create(
            name=request.form['name'],
            quantity=request.form['quantity']
        )
    return render_template('grocery.html', form=form,
                           shopping_list=shopping_list.getall())


@app.route('/grocery/delete/<uid>', methods=['POST'])
def grocery_delete(uid):
    shopping_list.delete(int(uid))
    return redirect(url_for('grocery'))


@app.route('/grocery/update/<uid>', methods=['GET', 'POST'])
def grocery_update(uid):
    form = UpdateItemForm()
    if form.validate_on_submit():
        shopping_list.update(
            uid=int(uid),
            name=request.form['name'],
            quantity=request.form['quantity']
        )
        return redirect(url_for('grocery'))
    return render_template('update.html', form=form,
                           item=shopping_list.get(int(uid)))
