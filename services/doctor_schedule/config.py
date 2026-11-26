# Team configuration
T = None  ######################################

CLINIC_NAME = f"MediBook-{T}" if T is not None else "MediBook-T"

# Doctor & Schedule Service
SERVICE_NAME = "doctor_schedule"
SERVICE_PORT = 5002

# Database
DB_HOST     = "localhost"
DB_PORT     = 3306
DB_NAME     = "clinic_system"
DB_USER     = "clinic_user"
DB_PASSWORD = "Password123*"

# Other service URLs
APPOINTMENT_SERVICE_URL  = "http://localhost:5001"
BILLING_SERVICE_URL      = "http://localhost:5003"
PATIENT_SERVICE_URL      = "http://localhost:5004"
NOTIFICATION_SERVICE_URL = "http://localhost:5005"

REQUEST_TIMEOUT = 3
