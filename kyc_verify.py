from flask import Blueprint, request, jsonify
import os

bp = Blueprint('kyc', __name__)

@bp.route('/kyc/verify', methods=['POST'])
def verify_kyc():
    try:
        user_id = request.form.get('user_id')
        if not user_id:
            return jsonify({'error': 'Missing user_id'}), 400

        if 'id_card_image' not in request.files or 'selfie_image' not in request.files:
            return jsonify({'error': 'Missing required image files'}), 400

        id_card = request.files['id_card_image']
        selfie = request.files['selfie_image']

        save_path = f"./uploads/kyc/{user_id}/"
        os.makedirs(save_path, exist_ok=True)
        id_card.save(os.path.join(save_path, 'id_card.jpg'))
        selfie.save(os.path.join(save_path, 'selfie.jpg'))

        return jsonify({'message': 'KYC submitted'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
