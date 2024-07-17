from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(10))  # 'admin' or 'user'

class Train(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(64))
    destination = db.Column(db.String(64))
    total_seats = db.Column(db.Integer)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    train_id = db.Column(db.Integer, db.ForeignKey('train.id'))
    seats_booked = db.Column(db.Integer)
