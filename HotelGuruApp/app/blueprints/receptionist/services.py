from app.extensions import db
from app.models import Booking, Room, User, ExtraService, Bill # Felt�telezve a modelljeidet
from sqlalchemy import select, and_
from app.blueprints.receptionist.schemas import ReceptionistBookingResponseSchema, BillResponseSchema
# Import�lj m�s sz�ks�ges dolgokat

class ReceptionistService:

    @staticmethod
    def list_pending_bookings():
        # Implement�ld a visszaigazol�sra v�r� foglal�sok list�z�s�t
        try:
            pending_bookings = Booking.query.filter_by(status='Created').all()
            return True, ReceptionistBookingResponseSchema(many=True).dump(pending_bookings)
            return True, [] 
        except Exception as e:
            return False, f"Failed to list pending bookings: {e}"

    @staticmethod
    def confirm_booking(booking_id):
        # Implement�ld a foglal�s visszaigazol�s�t
        # Keresd meg a foglal�st
        # Ellen�rizd a szoba el�rhet�s�g�t (ism�t ellen�rz�s, ha k�zben foglalt�k volna el)
        # M�dos�tsd a st�tuszt 'Confirmed'-re
        # Mentsd el
        try:

            booking = db.session.get(Booking, booking_id)
            if booking and booking.status == 'Created':
                # Ellen�rizd az el�rhet�s�get...
                booking.status = 'Confirmed'
                db.session.commit()
                return True, ReceptionistBookingResponseSchema().dump(booking)
            return False, "Booking not found or cannot be confirmed" 
        except Exception as e:
            db.session.rollback()
            return False, f"Failed to confirm booking: {e}"

    @staticmethod
    def check_in(booking_id):
        # Implement�ld a check-in logik�t
        # Keresd meg a foglal�st
        # Ellen�rizd a st�tuszt (legyen 'Confirmed')
        # M�dos�tsd a st�tuszt 'Checked-In'-re (vagy hasonl�)
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
        # Implement�ld a check-out �s sz�ml�z�si logik�t
        # Keresd meg a foglal�st
        # Ellen�rizd a st�tuszt (legyen 'Checked-In')
        # Kalkul�ld ki a teljes k�lts�get (sz�ll�s + extra szolg�ltat�sok)
        # Hozd l�tre a sz�ml�t
        # M�dos�tsd a foglal�s st�tusz�t 'Checked-Out'-ra
        # Mentsd el az adatb�zisba
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
        # Implement�ld a sz�mla lek�rdez�s�t foglal�s ID alapj�n
        try:

            bill = Bill.query.filter_by(booking_id=booking_id).first()
            if bill:
                return True, BillResponseSchema().dump(bill)
            return False, "Bill not found for this booking"
        except Exception as e:
            return False, f"Failed to get bill: {e}"