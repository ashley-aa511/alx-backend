#!/usr/bin/env python3
#4-app.py

"""
Imports modules to run the application
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)

#Configuration class
class Config:
    """
    Employs languages we need in this case English and French
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

#Apply configuration to your class app
app.config.from_object(Config)

babel = Babel(app)

# Locale Selector Function
@babel.localeselector
def get_locale():
    # Check if a 'locale' parameter exists in the URL and if it is supported
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(f"Locale from URL: {locale}")
        return locale
    # Fallback to the best match from the request's Accept-Language header
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    print(f"Best match from headers: {best_match}")
    return best_match

babel.init_app(app)

# Route module
@app.route('/')
def home(): 
    return render_template('4-index.html', home_title=_("home_title"), home_header=_("home_header"))


if __name__ == '__main__':
    app.run(debug=True)

