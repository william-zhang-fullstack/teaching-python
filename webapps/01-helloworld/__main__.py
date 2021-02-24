from flask import Flask  # pre-code for Flask webapps


app = Flask(__name__)  # the webapp itself


@app.route('/')  # how Flask specifies webpages
def index():
    return '<h1>Hello world</h1>'


if __name__ == '__main__':  # this runs the app
    app.run()
