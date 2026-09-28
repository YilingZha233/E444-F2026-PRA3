# Activity 1.1 and 1.2
# from flask import Flask, render_template
# from flask_bootstrap import Bootstrap

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, {}!</h1>'.format(name)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name = name)

# bootstrap = Bootstrap(app)

#Activity 1.3 
from datetime import datetime

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template(
        'index.html',
        name='Yiling',
        current_time=datetime.utcnow()
    )


@app.route('/user/<name>')
def user(name):
    return render_template(
        'user.html',
        name=name
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
