from marshmallow import Schema, fields
from apiflask.fields import Date, String, Email, Nested, Integer, List
from apiflask.validators import Length, OneOf, Email

from app.blueprints.guest.schemas import RoomResponseSchema, GuestRegisterSchema 

class ReceptionistBookingResponseSchema(Schema):
    id = Integer(dump_only=True)
    user = Nested(GuestRegisterSchema, dump_only=True) 
    room = Nested(RoomResponseSchema, dump_only=True) 
    check_in_date = Date(dump_only=True)
    check_out_date = Date(dump_only=True)
    status = String(dump_only=True)

class BillResponseSchema(Schema):
    id = Integer(dump_only=True)
    booking_id = Integer(dump_only=True)
    booking = Nested(ReceptionistBookingResponseSchema, dump_only=True) 
    items = List(String(), dump_only=True) 
    total_amount = Integer(dump_only=True)
    issue_date = Date(dump_only=True)
