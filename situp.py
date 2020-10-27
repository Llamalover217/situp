from flask import Flask, render_template, g, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():    # defines the home page
    # it tells the computer what the file is called that it needs to bring up
    return render_template('home.html')

if __name__ == '__main__':    # this runs the application
    app.run(debug=True)
