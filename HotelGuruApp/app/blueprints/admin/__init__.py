from apiflask import APIBlueprint

bp = APIBlueprint('admin', __name__, tag="Admin")

from app.blueprints.admin import routes