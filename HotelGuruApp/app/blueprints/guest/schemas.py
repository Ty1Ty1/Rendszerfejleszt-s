from app.extensions import ma 
from apiflask.fields import String, Integer, Date, List, Nested

class GuestRegisterSchema(ma.Schema):
    username = String(required=True)
    email = String(required=True)
    password = String(required=True)
    phone_number = String()
    address = String()

class GuestLoginSchema(ma.Schema):
    email = String(required=True)
    password = String(required=True)

class GuestProfileUpdateSchema(ma.Schema):
    phone_number = String()
    address = String()
    email = String() 

class RoomResponseSchema(ma.Schema):
    id = Integer(dump_only=True)
    room_number = String(dump_only=True)
    capacity = Integer(dump_only=True)
    price_per_night = Integer(dump_only=True)
    description = String(dump_only=True)
    equipment = List(String(), dump_only=True) 

class BookingRequestSchema(ma.Schema):
    room_id = Integer(required=True)
    check_in = Date(required=True)
    check_out = Date(required=True)

class BookingResponseSchema(ma.Schema):
    id = Integer(dump_only=True)
    room = Nested(RoomResponseSchema, dump_only=True) 
    check_in = Date(dump_only=True)
    check_out = Date(dump_only=True)
    status = String(dump_only=True) 
    total_price = Integer(dump_only=True) 

class ExtraServiceRequestSchema(ma.Schema):
    service_name = String(required=True)
    quantity = Integer(required=True)