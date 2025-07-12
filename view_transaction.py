from flask import Blueprint, render_template, request
from db import supabase

view_tx = Blueprint("view_tx", __name__)

@view_tx.route("/tx/<tx_id>")
def view_transaction(tx_id):
    pin = request.args.get("pin")
    role = request.args.get("role")  # buyer หรือ seller

    if not pin or role not in ["buyer", "seller"]:
        return "Missing or invalid parameters", 400

    # ตรวจสอบธุรกรรม
    res = supabase.table("transactions").select("*").eq("id", tx_id).eq("pin_code", pin).single().execute()
    tx = res.data
    if not tx:
        return "ไม่พบธุรกรรมหรือ PIN ไม่ถูกต้อง", 404

    # ดึงสลิป (payment)
    pay = supabase.table("payment_proofs").select("*").eq("transaction_id", tx_id).limit(1).execute().data
    slip_url = pay[0]["image_url"] if pay else None

    # ดึงข้อมูลการจัดส่ง
    ship = supabase.table("shipment_proofs").select("*").eq("transaction_id", tx_id).limit(1).execute().data
    shipment = ship[0] if ship else None

    return render_template("transaction_view.html", tx=tx, role=role, slip_url=slip_url, shipment=shipment)