from app.extensions import db
from app.models.user import User
from app.models.room import Room
from app.models.booking import Booking
from sqlalchemy import select, and_
from app.blueprints.receptionist.schemas import ReceptionistBookingResponseSchema, BillResponseSchema

class ReceptionistService:

    @staticmethod
    def list_pending_bookings():
        try:
            pending_bookings = Booking.query.filter_by(status='Created').all()
            return True, ReceptionistBookingResponseSchema(many=True).dump(pending_bookings)
            return True, [] 
        except Exception as e:
            return False, f"Failed to list pending bookings: {e}"

    @staticmethod
    def confirm_booking(booking_id):
        try:
            booking = db.session.get(Booking, booking_id)
            if booking and booking.status == 'Created':
                booking.status = 'Confirmed'
                db.session.commit()
                return True, ReceptionistBookingResponseSchema().dump(booking)
            return False, "Booking not found or cannot be confirmed" 
        except Exception as e:
            db.session.rollback()
            return False, f"Failed to confirm booking: {e}"

    @staticmethod
    def check_in(booking_id):
        try:
            booking = db.session.get(Booking, booking_id)
            if booking and booking.status == 'Confirmed':
                booking.status = 'Checked-In'
                db.session.commit()
                return True, ReceptionistBookingResponseSchema().dump(booking)
            return False, "Booking not found or cannot be checked in"
        except Exception as e:
            db.session.rollback()
            return False, f"Failed to check in: {e}"

    @staticmethod
    def check_out_and_generate_bill(booking_id):
        try:
            booking = db.session.get(Booking, booking_id)
            if booking and booking.status == 'Checked-In':
                new_bill = Bill(booking_id=booking_id, total_amount=calculated_amount)
                db.session.add(new_bill)
                booking.status = 'Checked-Out'
                db.session.commit()
                return True, BillResponseSchema().dump(new_bill)
            return False, "Check-out and billing not implemented or allowed"
        except Exception as e:
            db.session.rollback()
            return False, f"Check-out and billing failed: {e}"

    @staticmethod
    def get_bill(booking_id):
        try:

            bill = Bill.query.filter_by(booking_id=booking_id).first()
            if bill:
                return True, BillResponseSchema().dump(bill)
            return False, "Bill not found for this booking"
        except Exception as e:
            return False, f"Failed to get bill: {e}"
