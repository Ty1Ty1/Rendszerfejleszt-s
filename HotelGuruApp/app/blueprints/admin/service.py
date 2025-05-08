from app.extensions import db
from app.models.room import Room 
from app.blueprints.admin.schemas import RoomAdminResponseSchema
from sqlalchemy import select, and_

class AdminService:

    @staticmethod
    def list_all_rooms():
        try:

            all_rooms = Room.query.all()
            return True, RoomAdminResponseSchema(many=True).dump(all_rooms)
            return True, [] 
        except Exception as e:
            return False, f"Failed to list rooms: {e}"

    @staticmethod
    def create_room(data):
        try:
            new_room = Room(room_number=data['room_number'])
            db.session.add(new_room)
            db.session.commit()
            return True, RoomAdminResponseSchema().dump(new_room)
            return False, "Room creation not implemented" 
        except Exception as e:
            db.session.rollback()
            return False, f"Room creation failed: {e}"

    @staticmethod
    def get_room_details(room_id):
        try:

            room = db.session.get(Room, room_id)
            if room:
                return True, RoomAdminResponseSchema().dump(room)
            return False, "Room not found"
        except Exception as e:
            return False, f"Failed to get room details: {e}"

    @staticmethod
    def update_room(room_id, data):
        try:
            room = db.session.get(Room, room_id)
            if room:
                for key, value in data.items():
                    setattr(room, key, value)
                db.session.commit()
                return True, RoomAdminResponseSchema().dump(room)
            return False, "Room not found or update failed" 
        except Exception as e:
            db.session.rollback()
            return False, f"Room update failed: {e}"

    @staticmethod
    def delete_room(room_id):
        try:
            room = db.session.get(Room, room_id)
            if room and not room.has_active_bookings(): 
                db.session.delete(room)
                db.session.commit()
                return True, "Room deleted successfully"
            return False, "Room not found or cannot be deleted" 
        except Exception as e:
            db.session.rollback()
            return False, f"Room deletion failed: {e}"

    @staticmethod
    def update_room_status(room_id, status):
        try:
            room = db.session.get(Room, room_id)
            if room:
                room.status = status
                db.session.commit()
                return True, RoomAdminResponseSchema().dump(room)
            return False, "Room not found or status update failed" 
        except Exception as e:
            db.session.rollback()
            return False, f"Room status update failed: {e}"
