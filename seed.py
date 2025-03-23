from models import app, db, User, Room, Booking, Service, Invoice
from datetime import datetime, timedelta

# Create some sample users
def create_users():
    users = [
        User(username="john_doe", email="john@example.com", password="password123", role="guest"),
        User(username="jane_smith", email="jane@example.com", password="password123", role="receptionist"),
        User(username="admin", email="admin@example.com", password="admin123", role="admin"),
    ]
    db.session.add_all(users)
    db.session.commit()

# Create some sample rooms
def create_rooms():
    rooms = [
        Room(number="101", type="Single", price=100.0),
        Room(number="102", type="Double", price=150.0),
        Room(number="201", type="Suite", price=300.0),
        Room(number="202", type="Single", price=90.0),
    ]
    db.session.add_all(rooms)
    db.session.commit()

# Create some sample bookings
def create_bookings():
    bookings = [
        Booking(user_id=1, room_id=1, check_in=datetime.now(), check_out=datetime.now() + timedelta(days=2), status="confirmed"),
        Booking(user_id=2, room_id=2, check_in=datetime.now() + timedelta(days=1), check_out=datetime.now() + timedelta(days=3), status="pending"),
    ]
    db.session.add_all(bookings)
    db.session.commit()

# Create some sample services
def create_services():
    services = [
        Service(name="Room Service", price=25.0),
        Service(name="Spa", price=50.0),
        Service(name="Laundry", price=10.0),
    ]
    db.session.add_all(services)
    db.session.commit()

# Create some sample invoices
def create_invoices():
    invoices = [
        Invoice(user_id=1, total_amount=250.0, created_at=datetime.now()),
        Invoice(user_id=2, total_amount=400.0, created_at=datetime.now() + timedelta(days=1)),
    ]
    db.session.add_all(invoices)
    db.session.commit()

# Seed the database
with app.app_context():
    db.create_all()  # Create tables
    create_users()
    create_rooms()
    create_bookings()
    create_services()
    create_invoices()

    print("Database seeded successfully.")
