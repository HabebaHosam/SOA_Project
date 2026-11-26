from flask import Blueprint, jsonify, request
from db import get_connection

doctors_bp = Blueprint("doctors", __name__)


# ------------------------------------------------------------------
# GET /api/doctors
# Returns all doctors, with optional ?specialty= filter
# ------------------------------------------------------------------
@doctors_bp.route("/api/doctors", methods=["GET"])
def get_doctors():
    specialty = request.args.get("specialty")

    conn   = None
    cursor = None
    try:
        conn   = get_connection()
        cursor = conn.cursor(dictionary=True)

        if specialty:
            cursor.execute(
                "SELECT * FROM doctors WHERE specialty = %s",
                (specialty,)
            )
        else:
            cursor.execute("SELECT * FROM doctors")

        doctors = cursor.fetchall()

        for d in doctors:
            d["consultation_fee"] = float(d["consultation_fee"])

        return jsonify({"doctors": doctors}), 200

    except Exception as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500

    finally:
        if cursor: cursor.close()
        if conn:   conn.close()


# ------------------------------------------------------------------
# GET /api/doctors/<doctor_id>
# Returns a single doctor by ID
# ------------------------------------------------------------------
@doctors_bp.route("/api/doctors/<doctor_id>", methods=["GET"])
def get_doctor(doctor_id):

    # Validate: must be a positive integer
    try:
        doctor_id = int(doctor_id)
        if doctor_id <= 0:
            raise ValueError
    except ValueError:
        return jsonify({"error": "Invalid doctor_id. Must be a positive integer."}), 400

    conn   = None
    cursor = None
    try:
        conn   = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM doctors WHERE doctor_id = %s",
            (doctor_id,)
        )
        doctor = cursor.fetchone()

        if doctor is None:
            return jsonify({"error": f"Doctor {doctor_id} not found."}), 404

        doctor["consultation_fee"] = float(doctor["consultation_fee"])
        return jsonify({"doctor": doctor}), 200

    except Exception as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500

    finally:
        if cursor: cursor.close()
        if conn:   conn.close()
