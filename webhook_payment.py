from flask import Blueprint, request, jsonify

bp = Blueprint('webhook', __name__)

@bp.route('/webhook/payment', methods=['POST'])
def webhook_payment():
    try:
        data = request.get_json(force=True)
        if not data:
            return jsonify({'error': 'Empty webhook payload'}), 400
        print(f"Received Webhook: {data}")
        return jsonify({'message': 'Received'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500