from flask import Flask, render_template  # pre-code for Flask webapps


app = Flask(__name__)  # the webapp itself


@app.route('/')  # how Flask specifies webpages
def index():
    return render_template('index.html', msg='Hello world')


@app.route('/grocery')  # shopping list page
def grocery():
    shopping_list = [
        {'name': 'apple', 'quantity': 5},
        {'name': 'milk', 'quantity': '1 gallon'}
    ]
    return render_template('grocery.html', shopping_list=shopping_list)


if __name__ == '__main__':  # this runs the app
    app.run()
