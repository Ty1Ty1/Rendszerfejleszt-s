
from flask import Blueprint

bp = Blueprint('main', __name__)

# Importáljuk a routes.py-t
from app.blueprints.main import routes
