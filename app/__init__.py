from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from config import setup_logging
from .routes import main 

load_dotenv()

def create_app():
    """ Create and configure an instance of the Flask application. """

    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    setup_logging()

    app.register_blueprint(main)

    return app

