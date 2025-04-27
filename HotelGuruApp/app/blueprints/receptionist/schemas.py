from app.extensions import ma
from apiflask.fields import String, Integer, Date, Nested, List
from app.blueprints.guest.schemas import RoomResponseSchema, GuestResponseSchema 

class ReceptionistBookingResponseSchema(ma.Schema):
    id = Integer(dump_only=True)
    user = Nested(GuestResponseSchema, dump_only=True) 
    room = Nested(RoomResponseSchema, dump_only=True) 
    check_in_date = Date(dump_only=True)
    check_out_date = Date(dump_only=True)
    status = String(dump_only=True)

class BillResponseSchema(ma.Schema):
    id = Integer(dump_only=True)
    booking_id = Integer(dump_only=True)
    booking = Nested(ReceptionistBookingResponseSchema, dump_only=True) 
    items = List(String(), dump_only=True) 
    total_amount = Integer(dump_only=True)
    issue_date = Date(dump_only=True)
