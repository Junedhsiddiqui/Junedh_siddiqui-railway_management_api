from flask import Blueprint, request, jsonify
from app import db
from app.models import Train
from app.services.auth_service import admin_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/trains', methods=['POST'])
@admin_required
def add_train():
    data = request.get_json()
    new_train = Train(source=data['source'], destination=data['destination'], total_seats=data['total_seats'])
    db.session.add(new_train)
    db.session.commit()
    return jsonify({'message': 'Train added successfully'}), 201
