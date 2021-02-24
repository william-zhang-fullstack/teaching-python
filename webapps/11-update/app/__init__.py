import os
from flask import Flask
from app.database import ShoppingList


SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
shopping_list = ShoppingList()
from app import routes
