from flask import Blueprint, request, jsonify
import psycopg2
import os

bp = Blueprint('cancel_transaction', __name__)
DB_URL = os.environ.get("DATABASE_URL")

@bp.route('/cancel', methods=['POST'])
def cancel_transaction():
    try:
        data = request.get_json()
        transaction_id = data.get('transaction_id')
        if not transaction_id:
            return jsonify({'error': 'Missing transaction_id'}), 400

        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()

        # ตรวจสอบสถานะก่อนยกเลิก
        cur.execute("SELECT status FROM transactions WHERE id = %s", (transaction_id,))
        result = cur.fetchone()
        if not result:
            return jsonify({'error': 'Transaction not found'}), 404
        if result[0] != 'pending':
            return jsonify({'error': 'Only pending transactions can be cancelled'}), 400

        # อัปเดตเป็น cancelled
        cur.execute("UPDATE transactions SET status = 'cancelled' WHERE id = %s", (transaction_id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Transaction cancelled'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500