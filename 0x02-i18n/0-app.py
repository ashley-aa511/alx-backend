#!/usr/bin/env python3

#0-app.py
from flask import Flask, render_template
from flask_babel import Babel

app= Flask(__name__)

#Configuration class
class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

#Apply configuration to your class app
app.config.from_object(Config)

#Initialize Babel
babel = Babel(app)

@app.route('/')
def home():
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)
