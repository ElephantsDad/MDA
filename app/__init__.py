from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

socketio = SocketIO()
RLOC_IMG = 'none'
RLOC_NAME = 'none'

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///site.db'
    db = SQLAlchemy(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
