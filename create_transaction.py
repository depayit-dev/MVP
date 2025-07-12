from flask import Blueprint, request, jsonify
import uuid
import random
from db import supabase

create_tx = Blueprint("create_tx", __name__)

@create_tx.route("/transaction/create", methods=["POST"])
def create_transaction():
    try:
        data = request.json
        buyer_name = data.get("buyer_name")
        buyer_phone = data.get("buyer_phone")
        seller_phone = data.get("seller_phone")
        amount = data.get("amount")
        creator_role = data.get("creator_role")  # ต้องเป็น 'buyer' หรือ 'seller'

        # ตรวจสอบข้อมูล
        if not all([buyer_name, buyer_phone, seller_phone, amount, creator_role]):
            return jsonify({"error": "ข้อมูลไม่ครบ"}), 400
        if creator_role not in ["buyer", "seller"]:
            return jsonify({"error": "creator_role ต้องเป็น buyer หรือ seller"}), 400

        # สร้าง UUID และ PIN
        tx_id = str(uuid.uuid4())
        pin_code = str(random.randint(1000, 9999))

        # บันทึกธุรกรรมลง Supabase
        supabase.table("transactions").insert({
            "id": tx_id,
            "buyer_name": buyer_name,
            "buyer_phone": buyer_phone,
            "seller_phone": seller_phone,
            "amount": amount,
            "pin_code": pin_code
        }).execute()

        # สร้างลิงก์ตามบทบาท
        buyer_link = f"https://depayit.com/tx/{tx_id}?pin={pin_code}&role=buyer"
        seller_link = f"https://depayit.com/tx/{tx_id}?pin={pin_code}&role=seller"

        return jsonify({
            "status": "success",
            "transaction_id": tx_id,
            "pin_code": pin_code,
            "buyer_link": buyer_link,
            "seller_link": seller_link
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
