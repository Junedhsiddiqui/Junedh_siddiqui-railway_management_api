from flask import Blueprint, request, jsonify
from app import db
from app.models import Train, Booking
from app.services.auth_service import login_required

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/trains', methods=['GET'])
@login_required
def get_trains():
    source = request.args.get('source')
    destination = request.args.get('destination')
    trains = Train.query.filter_by(source=source, destination=destination).all()
    train_data = [{'id': train.id, 'source': train.source, 'destination': train.destination, 'available_seats': train.total_seats} for train in trains]
    return jsonify(train_data), 200
