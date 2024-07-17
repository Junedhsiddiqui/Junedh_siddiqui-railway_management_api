from app import db
from app.models import Booking, Train

def book_seat(user_id, train_id, seats_to_book):
    train = Train.query.get(train_id)
    if not train:
        return None
    
    if train.total_seats >= seats_to_book:
        booking = Booking(user_id=user_id, train_id=train_id, seats_booked=seats_to_book)
        db.session.add(booking)
        train.total_seats -= seats_to_book
        db.session.commit()
        return booking
    else:
        return None

def get_booking_details(booking_id):
    return Booking.query.get(booking_id)

# Add more functions as per requirements (cancel_booking, update_booking, etc.)
