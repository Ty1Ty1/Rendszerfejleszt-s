from app.blueprints.main import bp
from flask import Flask, render_template, request, redirect, url_for

# Home route
@bp.route('/')
def index():
    return render_template('register.html')

# Login route
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Add login logic (check credentials, etc.)
        return redirect(url_for('main.rooms'))  # Redirect to the rooms page after login
    return render_template('login.html')

# Register route
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Add registration logic (save user data, etc.)
        return redirect(url_for('main.login'))  # Redirect to login after registration
    return render_template('register.html')

# Rooms listing page
@bp.route('/rooms')
def rooms():
    # You can dynamically load room data here
    rooms = [{'name': 'Room 101', 'price': 100}, {'name': 'Room 102', 'price': 120}]
    return render_template('rooms.html', rooms=rooms)

# Booking page
@bp.route('/booking/<int:room_id>', methods=['GET', 'POST'])
def booking(room_id):
    if request.method == 'POST':
        # Process the booking (store it in the database, etc.)
        return redirect(url_for('booking_confirmation', room_id=room_id))  # Redirect to confirmation
    return render_template('booking.html', room_id=room_id)

# Booking confirmation page
@bp.route('/booking_confirmation/<int:room_id>')
def booking_confirmation(room_id):
    return render_template('booking_confirmation.html', room_id=room_id)

# Admin Dashboard
@bp.route('/admin_dashboard')
def admin_dashboard():
    # This can show various admin tasks (room management, bookings, etc.)
    return render_template('admin_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=8888)
