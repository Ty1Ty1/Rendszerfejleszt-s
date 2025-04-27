from app.extensions import ma
from apiflask.fields import String, Integer, List, Nested

from app.blueprints.guest.schemas import RoomResponseSchema

class RoomCreateUpdateSchema(ma.Schema):
    room_number = String(required=True)
    capacity = Integer(required=True)
    price_per_night = Integer(required=True)
    description = String()
    equipment = List(String()) 

class RoomAdminResponseSchema(ma.Schema):
    id = Integer(dump_only=True)
    room_number = String(dump_only=True)
    capacity = Integer(dump_only=True)
    price_per_night = Integer(dump_only=True)
    description = String(dump_only=True)
    equipment = List(String(), dump_only=True)
    status = String(dump_only=True) 

class RoomStatusUpdateSchema(ma.Schema):
    status = String(required=True) 