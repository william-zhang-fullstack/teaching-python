from flask import Flask, render_template  # pre-code for Flask webapps


app = Flask(__name__)  # the webapp itself


@app.route('/')  # how Flask specifies webpages
def index():
    return render_template('index.html', msg='Hello world')


if __name__ == '__main__':  # this runs the app
    app.run()
