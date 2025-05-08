#from flask import Blueprint
from apiflask import APIBlueprint
bp = APIBlueprint('main', __name__, tag="default")

from app.extensions import auth
from flask import current_app
from authlib.jose import jwt
from datetime import datetime
from apiflask import HTTPError

@auth.verify_token
def verify_token(token):
    try:
        data = jwt.decode(
            token.encode('ascii'),
           
            current_app.config['SECRET_KEY'],
        )
        if data["exp"] < int(datetime.now().timestamp()):
            return None
        return data
    except Exception as ex:
        return None

def role_required(roles):
    def wrapper(fn):
        def decorated_function(*args, **kwargs):
            user_roles = [item["name"] for item in auth.current_user.get("roles")]
            for role in roles:
                if role in user_roles:
                    return fn(*args, **kwargs)        
            raise HTTPError(message="Access denied", status_code=403)
        return decorated_function
    return wrapper


from app.blueprints.user import bp as bp_user
bp.register_blueprint(bp_user, url_prefix='/user')

from app.blueprints.admin import bp as bp_admin
bp.register_blueprint(bp_admin, url_prefix='/admin')

from app.blueprints.guest import bp as bp_guest
bp.register_blueprint(bp_guest, url_prefix='/guest')

from app.blueprints.receptionist import bp as bp_receptionist
bp.register_blueprint(bp_receptionist, url_prefix='/receptionist')

from app.models import *
