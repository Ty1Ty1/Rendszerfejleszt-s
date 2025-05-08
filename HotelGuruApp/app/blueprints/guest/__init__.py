#from flask import Blueprint
from apiflask import APIBlueprint

bp = APIBlueprint('guest', __name__, tag="guest")

from app.blueprints.guest import routes
