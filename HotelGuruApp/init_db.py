from __future__ import annotations

from app import db
from app import create_app
from config import Config

app = create_app(config_class=Config)

app.app_context().push()

#Role
from app.models.role import Role

db.session.add_all([ Role(name="Guest"), 
                     Role(name="User"), 
                     Role(name = "Receptionist"), 
                     Role(name ="Admin") ])
db.session.commit()




#Address
from app.models.address import Address
"""
db.session.add(Address( city = "Veszprém",  street = "Egyetem u. 1", postalcode=8200))
#db.session.commit()
"""

#User
from app.models.user import User, UserRestaurant, UserRole
"""
user = User(name="Test User", email="test@gmail.com", phone="+3620111111")
user.address = db.session.get(Address, 1)
user.set_password("qweasd")

db.session.add(user)

u = db.session.get(User, 1)
u.roles.append(db.session.get(Role,2))
u.roles.append(db.session.get(Role,4))

#db.session.commit()
"""

#Room
from app.models.room import Room
"""
room = Room(number = 123, price = 66000, type = "", status = available)

db.session.add(room)
#db.session.commit()
"""

#Booking
from app.models.booking import Booking
"""
booking = Booking(user_id = 1, room_id = 123, check_in = "2025.05.05" , check_out = "2025.05.06", status = "pending")
db.session.add(booking)

db.session.commit()
"""
