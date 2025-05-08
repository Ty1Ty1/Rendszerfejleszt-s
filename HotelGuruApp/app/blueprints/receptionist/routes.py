from app.blueprints.receptionist import bp
from app.blueprints.receptionist.schemas import (
    ReceptionistBookingResponseSchema, BillResponseSchema
)
from app.blueprints.receptionist.service import ReceptionistService
from apiflask import HTTPError
from apiflask.fields import Integer

@bp.get('/bookings/pending')
@bp.output(ReceptionistBookingResponseSchema(many=True))
def receptionist_list_pending_bookings():
    success, response = ReceptionistService.list_pending_bookings()
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


@bp.put('/bookings/<int:booking_id>/confirm')
@bp.output(ReceptionistBookingResponseSchema)
def receptionist_confirm_booking(booking_id):
    success, response = ReceptionistService.confirm_booking(booking_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.put('/bookings/<int:booking_id>/check-in')
@bp.output(ReceptionistBookingResponseSchema)
def receptionist_check_in(booking_id):
    success, response = ReceptionistService.check_in(booking_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.put('/bookings/<int:booking_id>/check-out')
@bp.output(BillResponseSchema) 
def receptionist_check_out(booking_id):
    success, response = ReceptionistService.check_out_and_generate_bill(booking_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400) 

@bp.get('/bookings/<int:booking_id>/bill')
@bp.output(BillResponseSchema)
def receptionist_get_bill(booking_id):
    success, response = ReceptionistService.get_bill(booking_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)
