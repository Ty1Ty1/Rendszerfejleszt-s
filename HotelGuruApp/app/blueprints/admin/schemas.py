from marshmallow import Schema, fields
from apiflask.fields import String, Email, Nested, Integer, List
from apiflask.validators import Length, OneOf, Email

from app.blueprints.guest.schemas import RoomResponseSchema

class RoomCreateUpdateSchema(Schema):
    room_number = String(required=True)
    capacity = Integer(required=True)
    price_per_night = Integer(required=True)
    description = String()
    equipment = List(String()) 

class RoomAdminResponseSchema(Schema):
    id = Integer(dump_only=True)
    room_number = String(dump_only=True)
    capacity = Integer(dump_only=True)
    price_per_night = Integer(dump_only=True)
    description = String(dump_only=True)
    equipment = List(String(), dump_only=True)
    status = String(dump_only=True) 

class RoomStatusUpdateSchema(Schema):
    status = String(required=True) 
