#from flask import Blueprint
from apiflask import APIBlueprint

bp = APIBlueprint('admin', __name__, tag="admin")

from app.blueprints.admin import routes
