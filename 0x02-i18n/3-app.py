#!/usr/bin/env python3
#2-app.py

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


#Locale Selector Function
@babel.localeselector
def get_locale():
    #This returns which language it decides to use
    return request.accept_languages.bestmatch(app.config['LANGUAGES'])

@app.route('/')
def home():
    return render_template('2-index.html', home_title=_('home_title'), home_header=_('home_header'))


if __name__ == '__main__':
    app.run(debug=True)



