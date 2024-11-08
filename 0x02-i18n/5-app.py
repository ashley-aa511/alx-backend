from flask import Flask, request, g, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Function to get a user based on login_as parameter
def get_user():
    user_id = request.args.get("login_as", type=int)
    if user_id in users:
        return users.get(user_id)
    return None

# before_request function to set g.user if a valid user is found
@app.before_request
def before_request():
    g.user = get_user()

# Basic route for demonstration
@app.route('/')
def index():
    return render_template('index.html')

# Babel configuration
@babel.localeselector_function
def get_locale():
    user = getattr(g, 'user', None)
    if user and user["locale"]:
        return user["locale"]
    return request.accept_languages.best_match(['en', 'fr'])

if __name__ == "__main__":
    app.run(debug=True)
