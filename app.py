from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_PATH = 'db.sqlite'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        buyer TEXT,
        seller TEXT,
        amount REAL,
        status TEXT,
        created_at TEXT
    )''')
    conn.commit()
    conn.close()

@app.route('/create', methods=['POST'])
def create_transaction():
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO transactions (buyer, seller, amount, status, created_at) VALUES (?, ?, ?, ?, ?)", 
              (data['buyer'], data['seller'], data['amount'], 'pending', datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Transaction created'}), 201

@app.route('/confirm', methods=['POST'])
def confirm_payment():
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE transactions SET status = 'confirmed' WHERE id = ?", (data['transaction_id'],))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Payment confirmed'}), 200

@app.route('/release', methods=['POST'])
def release_payment():
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE transactions SET status = 'released' WHERE id = ?", (data['transaction_id'],))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Payment released'}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
