from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    # shows the home page
    return 'Home Page'


@app.route('/about')
def about():
    # shows the about page
    return 'About'


@app.route('/user/<username>')
def user_profile(username):
    # shows user profile
    return 'User %s' % username
