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
# from datetime import datetime
# from flask import Flask, render_template
# from flask_bootstrap import Bootstrap
# from flask_moment import Moment

# app = Flask(__name__)

# bootstrap = Bootstrap(app)
# moment = Moment(app)


# @app.route('/')
# def index():
#     return render_template(
#         'index.html',
#         name='Yiling',
#         current_time=datetime.utcnow()
#     )


# @app.route('/user/<name>')
# def user(name):
#     return render_template(
#         'user.html',
#         name=name
#     )


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404


# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500



# Activity 1.4 
from datetime import datetime

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()

        # Name can be either first name or first name + last name.
        if not username:
            flash('Please enter your name.')
            return redirect(url_for('index'))

        # Check whether the user changed their name
        # compared with the previous submission.
        previous_name = session.get('name')

        if previous_name is not None and previous_name != username:
            flash("Looks like you've changed your name : )")

        # Save the current name for the next submission.
        session['name'] = username

        # Check that the email is a UofT email address.
        if 'utoronto' not in email.lower():
            flash('Please fill in a UofT email address.')
            return redirect(url_for('index'))

        return render_template(
            'index.html',
            name=username,
            email=email,
            submitted=True,
            current_time=datetime.utcnow()
        )

    return render_template(
        'index.html',
        name='Yiling',
        submitted=False,
        current_time=datetime.utcnow()
    )


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500