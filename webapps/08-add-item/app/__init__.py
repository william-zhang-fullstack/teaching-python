import os
from flask import Flask


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY  # CSRF tokens need this
shopping_list = []
from app import routes
