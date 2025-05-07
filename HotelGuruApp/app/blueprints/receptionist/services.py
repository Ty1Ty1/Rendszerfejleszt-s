from app.extensions import db
from app.models import Booking, Room, User, ExtraService, Bill # Feltételezve a modelljeidet
from sqlalchemy import select, and_
from app.blueprints.receptionist.schemas import ReceptionistBookingResponseSchema, BillResponseSchema
# Importálj más szükséges dolgokat

class ReceptionistService:

    @staticmethod
    def list_pending_bookings():
        # Implementáld a visszaigazolásra váró foglalások listázását
        try:
            pending_bookings = Booking.query.filter_by(status='Created').all()
            return True, ReceptionistBookingResponseSchema(many=True).dump(pending_bookings)
            return True, [] 
        except Exception as e:
            return False, f"Failed to list pending bookings: {e}"

    @staticmethod
    def confirm_booking(booking_id):
        # Implementáld a foglalás visszaigazolását
        # Keresd meg a foglalást
        # Ellenõrizd a szoba elérhetõségét (ismét ellenõrzés, ha közben foglalták volna el)
        # Módosítsd a státuszt 'Confirmed'-re
        # Mentsd el
        try:

            booking = db.session.get(Booking, booking_id)
            if booking and booking.status == 'Created':
                # Ellenõrizd az elérhetõséget...
                booking.status = 'Confirmed'
                db.session.commit()
                return True, ReceptionistBookingResponseSchema().dump(booking)
            return False, "Booking not found or cannot be confirmed" 
        except Exception as e:
            db.session.rollback()
            return False, f"Failed to confirm booking: {e}"

    @staticmethod
    def check_in(booking_id):
        # Implementáld a check-in logikát
        # Keresd meg a foglalást
        # Ellenõrizd a státuszt (legyen 'Confirmed')
        # Módosítsd a státuszt 'Checked-In'-re (vagy hasonló)
        # Mentsd el
        try:
            booking = db.session.get(Booking, booking_id)
            if booking and booking.status == 'Confirmed':
                booking.status = 'Checked-In'
                db.session.commit()
                return True, ReceptionistBookingResponseSchema().dump(booking)
            return False, "Booking not found or cannot be checked in" # Placeholder
        except Exception as e:
            db.session.rollback()
            return False, f"Failed to check in: {e}"

    @staticmethod
    def check_out_and_generate_bill(booking_id):
        # Implementáld a check-out és számlázási logikát
        # Keresd meg a foglalást
        # Ellenõrizd a státuszt (legyen 'Checked-In')
        # Kalkuláld ki a teljes költséget (szállás + extra szolgáltatások)
        # Hozd létre a számlát
        # Módosítsd a foglalás státuszát 'Checked-Out'-ra
        # Mentsd el az adatbázisba
        try:
            booking = db.session.get(Booking, booking_id)
            if booking and booking.status == 'Checked-In':
                new_bill = Bill(booking_id=booking_id, total_amount=calculated_amount)
                db.session.add(new_bill)
                booking.status = 'Checked-Out'
                db.session.commit()
                return True, BillResponseSchema().dump(new_bill)
            return False, "Check-out and billing not implemented or allowed" # Placeholder
        except Exception as e:
            db.session.rollback()
            return False, f"Check-out and billing failed: {e}"

    @staticmethod
    def get_bill(booking_id):
        # Implementáld a számla lekérdezését foglalás ID alapján
        try:

            bill = Bill.query.filter_by(booking_id=booking_id).first()
            if bill:
                return True, BillResponseSchema().dump(bill)
            return False, "Bill not found for this booking"
        except Exception as e:
            return False, f"Failed to get bill: {e}"