from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page'

@app.route('/about')
def about():
    return 'About'

@app.route('/user/<username>')
def user_profile(username):
    return 'User %s' username
