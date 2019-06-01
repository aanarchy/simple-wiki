from flask import render_template
from liberalmemes import app


@app.route('/')
def home():
    return 'Home Page'


@app.route('/about')
def about():
    return 'About'


@app.route('/home')
def index():
    user = {'username': 'anarchy'}
    posts = [
        {
            'author': {'username': 'faith'},
            'body': '11/10'
        },
        {
            'author': {'username': 'skeppy'},
            'body': '666'
        }
    ]
    return render_template('home.html', title="Home", user=user, posts=posts)


@app.route('/user/<username>')
def user_profile(username):
    return 'User %s' % username
