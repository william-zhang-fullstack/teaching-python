import os
from flask import Flask
from app.database import ShoppingList


SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
shopping_list = ShoppingList()
shopping_list.create('bread', '1 loaf')
shopping_list.create('eggs', '1 dozen')
shopping_list.create('milk', '1 gallon')
shopping_list.create('banana', '1 pound')
from app import routes
