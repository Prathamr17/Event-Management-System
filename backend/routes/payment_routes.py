from flask import Blueprint, jsonify
import qrcode

payment_bp = Blueprint("payments", __name__)

@payment_bp.route("/upi", methods=["GET"])
def upi_qr():
    url = "upi://pay?pa=pratham.raikar@fam&pn=EMS"
    img = qrcode.make(url)
    img.save("upi_qr.png")
    return jsonify(message="UPI QR generated")
