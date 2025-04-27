from app.blueprints.receptionist import bp
from app.blueprints.receptionist.schemas import (
    ReceptionistBookingResponseSchema, BillResponseSchema
)
from app.blueprints.receptionist.service import ReceptionistService
from apiflask import HTTPError, output, abort
from apiflask.fields import Integer

# @auth_required # Recepciós szerepkör ellenõrzése szükséges lehet

@bp.get('/bookings/pending')
@output(ReceptionistBookingResponseSchema(many=True))
def receptionist_list_pending_bookings():
    success, response = ReceptionistService.list_pending_bookings()
    if success:
        return response, 200
    abort(400, message=response)


@bp.put('/bookings/<int:booking_id>/confirm')
@output(ReceptionistBookingResponseSchema)
def receptionist_confirm_booking(booking_id):
    success, response = ReceptionistService.confirm_booking(booking_id)
    if success:
        return response, 200
    abort(400, message=response)

@bp.put('/bookings/<int:booking_id>/check-in')
@output(ReceptionistBookingResponseSchema)
def receptionist_check_in(booking_id):
    success, response = ReceptionistService.check_in(booking_id)
    if success:
        return response, 200
    abort(400, message=response) 

@bp.put('/bookings/<int:booking_id>/check-out')
@output(BillResponseSchema) 
def receptionist_check_out(booking_id):
    success, response = ReceptionistService.check_out_and_generate_bill(booking_id)
    if success:
        return response, 200
    abort(400, message=response) 

@bp.get('/bookings/<int:booking_id>/bill')
@output(BillResponseSchema)
def receptionist_get_bill(booking_id):
    success, response = ReceptionistService.get_bill(booking_id)
    if success:
        return response, 200
    abort(404, message=response) 