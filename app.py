# imports
from flask import Flask, render_template
from flask_socketio import SocketIO

# setups and global variables
app = Flask(__name__)
socketio = SocketIO(app)

# app routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/committees')
def resources():
    return render_template('committees.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# CALLING EVERYTHING TOGETHER
if __name__ == '__main__':
    socketio.run(app)