from flask import Flask  # pre-code for Flask webapps


app = Flask(__name__)  # the webapp itself
shopping_list = [
    {'name': 'apple', 'quantity': 5},
    {'name': 'milk', 'quantity': '1 gallon'}
]
from app import routes  # need this or routes will not generate
