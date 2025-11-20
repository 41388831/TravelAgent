from flask import Flask

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes

    return app
