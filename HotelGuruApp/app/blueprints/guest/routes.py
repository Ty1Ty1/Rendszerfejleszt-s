from app.blueprints.guest import bp
from app.blueprints.guest.schemas import (
    GuestRegisterSchema, GuestLoginSchema, GuestProfileUpdateSchema,
    RoomResponseSchema, BookingRequestSchema, BookingResponseSchema,
    ExtraServiceRequestSchema
)
from app.blueprints.guest.service import GuestService
from apiflask import HTTPError, input, output, abort
from apiflask.fields import Integer

@bp.post('/register')
@input(GuestRegisterSchema)
@output({}, status_code=201) # Feltételezve, hogy a regisztráció sikeresen lezárul és nincs visszaadott tartalom
def guest_register(data):
    success, response = GuestService.register(data)
    if success:
        return response, 201
    abort(400, message=response)

@bp.post('/login')
@input(GuestLoginSchema)
# Itt a válasz schema a sikeres bejelentkezéshez szükséges adatokat (pl. token) tartalmazza
@output({'token': str}) # Példa: visszaad egy tokent
def guest_login(data):
    success, response = GuestService.login(data)
    if success:
        return {'token': response}, 200 # Példa: visszaadott tokent
    abort(401, message=response) # Helytelen hitelesítés

@bp.put('/profile')
@input(GuestProfileUpdateSchema)
# Dekorátor a bejelentkezett felhasználó ellenõrzéséhez szükséges lehet 
# @auth_required # Feltételezve egy hitelesítési dekorátort
@output({}, status_code=200)
def guest_update_profile(data):
    # user_id = get_current_user_id() # Feltételezve egy funkciót az aktuális felhasználó ID lekérdezésére
    success, response = GuestService.update_profile(user_id, data) # user_id átadása szükséges lehet
    if success:
        return response, 200
    abort(400, message=response)

@bp.get('/rooms')
@output(RoomResponseSchema(many=True))
def guest_list_rooms():
    success, response = GuestService.list_available_rooms()
    if success:
        return response, 200
    abort(400, message=response)


@bp.get('/rooms/<int:room_id>')
@output(RoomResponseSchema)
def guest_get_room(room_id):
    success, response = GuestService.get_room_details(room_id)
    if success:
        return response, 200
    abort(404, message=response) # Nem található szoba

@bp.post('/bookings')
@input(BookingRequestSchema)
# @auth_required
@output(BookingResponseSchema, status_code=201)
def guest_create_booking(data):
    # user_id = get_current_user_id()
    success, response = GuestService.create_booking(user_id, data)
    if success:
        return response, 201
    abort(400, message=response)

@bp.get('/bookings/<int:booking_id>')

@output(BookingResponseSchema)
def guest_get_booking(booking_id):
    user_id = get_current_user_id()
    success, response = GuestService.get_booking_details(user_id, booking_id)
    if success:
        return response, 200
    abort(404, message=response) 

@bp.delete('/bookings/<int:booking_id>')
@output({}, status_code=200)
def guest_cancel_booking(booking_id):
    user_id = get_current_user_id()
    success, response = GuestService.cancel_booking(user_id, booking_id)
    if success:
        return response, 200
    abort(400, message=response)

@bp.post('/bookings/<int:booking_id>/services')
@input(ExtraServiceRequestSchema)
# @auth_required
@output({}, status_code=200)
def guest_add_extra_service(booking_id, data):
    user_id = get_current_user_id()
    success, response = GuestService.add_extra_service(user_id, booking_id, data)
    if success:
        return response, 200
    abort(400, message=response) 