from flask import Blueprint, request, jsonify
from db import get_db
from datetime import datetime

bp = Blueprint('create', __name__)

@bp.route('/create', methods=['POST'])
def create_transaction():
    try:
        data = request.get_json(force=True)
        buyer = data.get('buyer')
        seller = data.get('seller')
        amount = data.get('amount')
        if not all([buyer, seller, amount]):
            return jsonify({'error': 'Missing buyer, seller or amount'}), 400

        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO transactions (buyer, seller, amount, status, created_at) VALUES (%s, %s, %s, %s, %s)",
                    (buyer, seller, amount, 'pending', datetime.utcnow()))
        conn.commit()
        return jsonify({'message': 'Transaction created'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500