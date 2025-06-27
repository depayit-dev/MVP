from flask import Flask, request, jsonify
import psycopg2
from datetime import datetime
import os

app = Flask(__name__)
DB_URL = os.environ.get("DATABASE_URL")

def init_db():
    conn = psycopg2.connect(DB_URL)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            buyer TEXT,
            seller TEXT,
            amount REAL,
            status TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/create', methods=['POST'])
def create_transaction():
    data = request.get_json()
    if not data or 'buyer' not in data or 'seller' not in data or 'amount' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    try:
        conn = psycopg2.connect(DB_URL)
        c = conn.cursor()
        c.execute(
            "INSERT INTO transactions (buyer, seller, amount, status, created_at) VALUES (%s, %s, %s, %s, %s)",
            (data['buyer'], data['seller'], data['amount'], 'pending', datetime.utcnow().isoformat())
        )
        conn.commit()
        conn.close()
        return jsonify({'message': 'Transaction created'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/confirm', methods=['POST'])
def confirm_payment():
    data = request.json
    conn = psycopg2.connect(DB_URL)
    c = conn.cursor()
    c.execute("UPDATE transactions SET status = 'confirmed' WHERE id = %s", (data['transaction_id'],))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Payment confirmed'}), 200

@app.route('/release', methods=['POST'])
def release_payment():
    data = request.get_json()
    if not data or 'transaction_id' not in data:
        return jsonify({'error': 'Missing transaction_id'}), 400
    try:
        conn = psycopg2.connect(DB_URL)
        c = conn.cursor()
        c.execute("UPDATE transactions SET status = 'released' WHERE id = %s", (data['transaction_id'],))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Payment released'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/init', methods=['GET'])
def initialize_database():
    try:
        init_db()
        return jsonify({'message': 'Database initialized'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
