# Team configuration
T = None  # Replace with your team number later

CLINIC_NAME = f"MediBook-{T}" if T is not None else "MediBook-T"

BOOKING_FEE = 20 + T if T is not None else None

LOYALTY_THRESHOLD = (
    3 + (T % 3) if T is not None else None
)

# Appointment Service
SERVICE_NAME = "appointment"
SERVICE_PORT = 5001

# Database configuration
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "clinic_system"
DB_USER = "clinic_user"
DB_PASSWORD = "YOUR_DATABASE_PASSWORD"

# Service URLs
DOCTOR_SERVICE_URL = "http://localhost:5002"
BILLING_SERVICE_URL = "http://localhost:5003"
PATIENT_SERVICE_URL = "http://localhost:5004"
NOTIFICATION_SERVICE_URL = "http://localhost:5005"

REQUEST_TIMEOUT = 3
