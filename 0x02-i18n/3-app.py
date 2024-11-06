#!/usr/bin/env python3
#3-app.py

#Imports modules important for the application to work
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)

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
    return render_template('2-index.html', home_title=_('home_title'), home_header=_('home_header'))


if __name__ == '__main__':
    app.run(debug=True)


