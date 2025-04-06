from app import db, create_app
from config import Config

# Setup app and context
app = create_app(Config)
app.app_context().push()

# Import all models BEFORE calling create_all
from app.models.user import User
from app.models.role import Role
from app.models.association import UserRole

# Create tables
db.drop_all()
db.create_all()

# Add roles
guest = Role(name="Guest")
user_role = Role(name="User")
receptionist_role = Role(name="Receptionist")
admin = Role(name="Admin")
db.session.add_all([guest, user_role, receptionist_role, admin])

#Address
from app.models.address import Address

db.session.add(Address( city = "Veszprem",  street = "Egyetem u. 1", postalcode=8200))
#db.session.commit()

# Add user
user = User(username="Test User", email="test@gmail.com", phone="+3620111111")
user.address = db.session.get(Address, 1)
user.set_password("qweasd")
db.session.add(user)

# Flush before assigning role
db.session.flush()

# Assign role to user safely
from sqlalchemy.exc import NoResultFound

with db.session.no_autoflush:
    u = db.session.get(User, 1)
    r = db.session.get(Role, 2)
    if u and r:
        u.roles.append(r)

# Commit everything
db.session.commit()

db.drop_all()