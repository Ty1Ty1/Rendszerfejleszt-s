from HotelGuruApp.app.blueprints.guest.schemas import ExtraServiceRequestSchema
from app.extensions import db 
from app.models.user import User
from app.models.room import Room
from app.models.booking import Booking
from app.blueprints.guest.schemas import RoomResponseSchema, BookingResponseSchema
from sqlalchemy import select, and_

class GuestService:

    @staticmethod
    def register(data):
        try:
            new_user = User(username=data['username'], email=data['email'], )
            new_user.set_password(data['password'])
            db.session.add(new_user)
            db.session.commit()
            return True, "User registered successfully"
        except Exception as e:
            db.session.rollback()
            return False, f"Registration failed: {e}"

    @staticmethod
    def login(data):
        try:
            user = User.query.filter_by(email=data['email']).first()
            if user and user.check_password(data['password']):
                token = generate_auth_token(user.id)
                return True, token
            return False, "Invalid credentials"
        except Exception as e:
            return False, f"Login failed: {e}"

    @staticmethod
    def update_profile(user_id, data):
        try:
            user = db.session.get(User, user_id)
            if user:
                for key, value in data.items():
                    setattr(user, key, value)
                db.session.commit()
                return True, "Profile updated successfully"
            return False, "User not found"
        except Exception as e:
            db.session.rollback()
            return False, f"Profile update failed: {e}"

    @staticmethod
    def list_available_rooms():
        try:
            available_rooms = Room.query.filter_by(status='Available').all()
            return True, RoomResponseSchema(many=True).dump(available_rooms)
        except Exception as e:
            return False, f"Failed to list rooms: {e}"

    @staticmethod
    def get_room_details(room_id):
        try:
            room = db.session.get(Room, room_id)
            if room:
                return True, RoomResponseSchema().dump(room)
            return False, "Room not found"
        except Exception as e:
            return False, f"Failed to get room details: {e}"


    @staticmethod
    def create_booking(user_id, data):

        try:
            room = db.session.get(Room, data['room_id'])
            if not room:
                return False, "Room not found"
            new_booking = Booking(user_id=user_id, room_id=data['room_id'])
            db.session.add(new_booking)
            db.session.commit()
            return True, BookingResponseSchema().dump(new_booking)
            return False, "Booking creation not implemented" 
        except Exception as e:
            db.session.rollback()
            return False, f"Booking creation failed: {e}"


    @staticmethod
    def get_booking_details(user_id, booking_id):
        try:
            booking = db.session.execute(select(Booking).filter(Booking.id == booking_id, Booking.user_id == user_id)).scalar_one_or_none()
            if booking:
                return True, BookingResponseSchema().dump(booking)
            return False, "Booking not found or does not belong to user"
        except Exception as e:
            return False, f"Failed to get booking details: {e}"


    @staticmethod
    def cancel_booking(user_id, booking_id):
        try:
            booking = db.session.execute(select(Booking).filter(Booking.id == booking_id, Booking.user_id == user_id)).scalar_one_or_none()
            if not booking:
                return False, "Booking not found or does not belong to user"
            booking.status = 'Canceled'
            db.session.commit()
            return True, "Booking cancelled successfully"
        except Exception as e:
            db.session.rollback()
            return False, f"Booking cancellation failed: {e}"

    @staticmethod
    def add_extra_service(user_id, booking_id, data):
        try:
            booking = db.session.execute(select(Booking).filter(Booking.id == booking_id, Booking.user_id == user_id)).scalar_one_or_none()
            if not booking:
                return False, "Booking not found or does not belong to user"
            new_service = ExtraServiceRequestSchema(booking_id=booking_id, name=data['service_name'], quantity=data['quantity'])
            db.session.add(new_service)
            db.session.commit()
            return False, "Adding extra service not implemented"
        except Exception as e:
            db.session.rollback()
            return False, f"Failed to add extra service: {e}"
