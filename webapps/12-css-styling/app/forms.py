from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    submit = SubmitField('')


class UpdateItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    submit = SubmitField('')
