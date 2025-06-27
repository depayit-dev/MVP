from flask import Blueprint, request, jsonify
from db import get_db

bp = Blueprint('confirm', __name__)

@bp.route('/confirm', methods=['POST'])
def confirm_payment():
    try:
        data = request.get_json(force=True)
        transaction_id = data.get('transaction_id')
        if not transaction_id:
            return jsonify({'error': 'Missing transaction_id'}), 400

        conn = get_db()
        cur = conn.cursor()
        cur.execute("UPDATE transactions SET status = 'confirmed' WHERE id = %s", (transaction_id,))
        if cur.rowcount == 0:
            return jsonify({'error': 'Transaction not found'}), 404
        conn.commit()
        return jsonify({'message': 'Payment confirmed'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500