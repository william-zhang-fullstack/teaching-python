from flask_wtf import FlaskForm  # the form base class
from wtforms import StringField, SubmitField  # will turn into HTML elements
from wtforms.validators import DataRequired  # force user behavior


class NewItemForm(FlaskForm):
    # lets the user add a new item/quantity to the shopping list
    name = StringField('Name', validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Add new!')
