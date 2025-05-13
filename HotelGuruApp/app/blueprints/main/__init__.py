from apiflask import APIBlueprint

bp = APIBlueprint('main', __name__)


from app.blueprints.admin import bp as admin_bp
bp.register_blueprint(admin_bp)

from app.blueprints.guest import bp as guest_bp
bp.register_blueprint(guest_bp)

from app.blueprints.receptionist import bp as receptionist_bp
bp.register_blueprint(receptionist_bp)

from app.blueprints.user import bp as user_bp
bp.register_blueprint(user_bp)

# Importáljuk a routes.py-t
from app.blueprints.main import routes
