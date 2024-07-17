from app import db
from app.models import Train

def add_train(source, destination, total_seats):
    new_train = Train(source=source, destination=destination, total_seats=total_seats)
    db.session.add(new_train)
    db.session.commit()
    return new_train

def get_trains_between_stations(source, destination):
    return Train.query.filter_by(source=source, destination=destination).all()

# Add more functions as per requirements (update_train, delete_train, etc.)
