from apiflask import APIBlueprint

bp = APIBlueprint('guest', __name__, tag="Guest")

from app.blueprints.guest import routes