from app.blueprints.guest import bp
from app.blueprints.guest.schemas import (
    GuestRegisterSchema, GuestLoginSchema, GuestProfileUpdateSchema,
    RoomResponseSchema, BookingRequestSchema, BookingResponseSchema,
    ExtraServiceRequestSchema
)
from app.blueprints.guest.service import GuestService
from flask import request
from apiflask import HTTPError, APIFlask
from apiflask.fields import Integer
from flask_login import current_user
from marshmallow import ValidationError

def get_current_user_id():
    return current_user.id

@bp.post('/register')
def guest_register():
    schema = GuestRegisterSchema()
    try:
        # Load and validate incoming JSON data
        data = schema.load(request.json)
    except ValidationError as err:
        return {'message': str(err)}, 400

    success, response = GuestService.register(data)
    if success:
        return response, 201
    return {'message': response}, 400

@bp.post('/login')
@bp.input(GuestLoginSchema)
@bp.output({'token': str})
def guest_login(data):
    success, response = GuestService.login(data)
    if success:
        return {'token': response}, 200
    raise HTTPError(message=response, status_code=400)

@bp.put('/profile')
@bp.input(GuestProfileUpdateSchema)
@bp.output({}, status_code=200)
def guest_update_profile(data):
    user_id = get_current_user_id()
    success, response = GuestService.update_profile(user_id, data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.get('/rooms')
@bp.output(RoomResponseSchema(many=True))
def guest_list_rooms():
    success, response = GuestService.list_available_rooms()
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


@bp.get('/rooms/<int:room_id>')
@bp.output(RoomResponseSchema)
def guest_get_room(room_id):
    success, response = GuestService.get_room_details(room_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.post('/bookings')
@bp.input(BookingRequestSchema)
@bp.output(BookingResponseSchema, status_code=201)
def guest_create_booking(data):
    user_id = get_current_user_id()
    success, response = GuestService.create_booking(user_id, data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.get('/bookings/<int:booking_id>')
@bp.output(BookingResponseSchema)
def guest_get_booking(booking_id):
    user_id = get_current_user_id()
    success, response = GuestService.get_booking_details(user_id, booking_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.delete('/bookings/<int:booking_id>')
@bp.output({}, status_code=200)
def guest_cancel_booking(booking_id):
    user_id = get_current_user_id()
    success, response = GuestService.cancel_booking(user_id, booking_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.post('/bookings/<int:booking_id>/services')
@bp.input(ExtraServiceRequestSchema)
@bp.output({}, status_code=200)
def guest_add_extra_service(booking_id, data):
    user_id = get_current_user_id()
    success, response = GuestService.add_extra_service(user_id, booking_id, data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400) 
