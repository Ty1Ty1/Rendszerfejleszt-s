from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from models import db, User, Room, Booking  # Import db and models

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hotelguru.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database with the app
db.init_app(app)
migrate = Migrate(app, db)

# API Endpoints
@app.route("/")
def home():
    return jsonify({"message": "Welcome to HotelGuru API!"})

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{ "id": u.id, "username": u.username, "email": u.email, "role": u.role } for u in users])

@app.route("/rooms", methods=["GET"])
def get_rooms():
    rooms = Room.query.all()
    return jsonify([{ "id": r.id, "number": r.number, "type": r.type, "price": r.price, "available": r.status } for r in rooms])

@app.route("/bookings", methods=["GET"])
def get_bookings():
    bookings = Booking.query.all()
    return jsonify([{ 
        "id": b.id, 
        "user_id": b.user_id, 
        "room_id": b.room_id, 
        "check_in": b.check_in.strftime('%Y-%m-%d'), 
        "check_out": b.check_out.strftime('%Y-%m-%d') 
    } for b in bookings])

# Create a booking
@app.route("/bookings", methods=["POST"])
def create_booking():
    data = request.get_json()
    user_id = data.get('user_id')
    room_id = data.get('room_id')
    check_in = datetime.strptime(data.get('check_in'), '%Y-%m-%d %H:%M:%S.%f')
    check_out = datetime.strptime(data.get('check_out'), '%Y-%m-%d %H:%M:%S.%f')

    new_booking = Booking(user_id=user_id, room_id=room_id, check_in=check_in, check_out=check_out)
    db.session.add(new_booking)
    db.session.commit()

    return jsonify({"message": "Booking created successfully!", "id": new_booking.id}), 201

if __name__ == "__main__":
    app.run(debug=True)
