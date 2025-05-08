from apiflask import APIFlask, HTTPTokenAuth
from flask import Flask
from config import Config
from app.extensions import db
from app.models import *
from app.blueprints.main import bp as main_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(main_bp)

    return app
