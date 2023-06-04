# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# handle error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    # app.debug = True
    app.run()
