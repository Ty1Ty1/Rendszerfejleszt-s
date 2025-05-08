from marshmallow import Schema, fields
from apiflask.fields import Date, String, Email, Nested, Integer, List
from apiflask.validators import Length, OneOf, Email

class GuestRegisterSchema(Schema):
    username = String(required=True)
    email = String(required=True)
    password = String(required=True)
    phone_number = String()
    address = String()

class GuestLoginSchema(Schema):
    email = String(required=True)
    password = String(required=True)

class GuestProfileUpdateSchema(Schema):
    phone_number = String()
    address = String()
    email = String() 

class RoomResponseSchema(Schema):
    id = Integer(dump_only=True)
    room_number = String(dump_only=True)
    capacity = Integer(dump_only=True)
    price_per_night = Integer(dump_only=True)
    description = String(dump_only=True)
    equipment = List(String(), dump_only=True) 

class BookingRequestSchema(Schema):
    room_id = Integer(required=True)
    check_in = Date(required=True)
    check_out = Date(required=True)

class BookingResponseSchema(Schema):
    id = Integer(dump_only=True)
    room = Nested(RoomResponseSchema, dump_only=True) 
    check_in = Date(dump_only=True)
    check_out = Date(dump_only=True)
    status = String(dump_only=True) 
    total_price = Integer(dump_only=True) 

class ExtraServiceRequestSchema(Schema):
    service_name = String(required=True)
    quantity = Integer(required=True)
