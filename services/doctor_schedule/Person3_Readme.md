# Doctor & Schedule Service - Coordination Guide (Person 2 to Person 3)

## Overview

We share the **Doctor & Schedule Service** running on port `5002` under `services/doctor_schedule/`.
The base Flask application, configuration, and database connection helper are already set up on the `feature/person2-doctor-management` branch.

---

## Current Project Structure

```text
services/doctor_schedule/
├── app.py                 # Flask entry point + /health endpoint (shared)
├── config.py              # Service, DB, and team configuration (shared)
├── db.py                  # MySQL connection helper (shared)
├── requirements.txt       # Python dependencies (shared)
└── routes/
    ├── __init__.py
    ├── doctors.py         # Person 2 (completed)
    └── slots.py           # Person 3 (to be created by you)
```

---

## Shared Files and How to Use Them

### 1. `db.py` (Do not create a separate DB connection)
Use the existing `get_connection()` function in `db.py`:

```python
from db import get_connection
```

Example usage inside a route:

```python
conn = None
cursor = None
try:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    # your SQL queries here
    # remember conn.commit() after INSERT or UPDATE
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
```

### 2. `config.py` (Do not hardcode DB settings or ports)
All database credentials (`DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`) and service settings (`SERVICE_NAME`, `SERVICE_PORT`) are already defined in `config.py`.

### 3. `routes/slots.py` (Your route file)
Create `services/doctor_schedule/routes/slots.py` and define a Flask Blueprint named `slots_bp`:

```python
from flask import Blueprint, jsonify, request
from db import get_connection

slots_bp = Blueprint("slots", __name__)
```

Implement your assigned endpoints inside this blueprint:
- `GET /api/doctors/<doctor_id>/slots` (optional `?date=YYYY-MM-DD`)
- `GET /api/slots/<slot_id>`
- `PUT /api/slots/<slot_id>/reserve`
- `PUT /api/slots/<slot_id>/release`

### 4. `app.py` (Registering your blueprint)
Currently `app.py` only registers `doctors_bp` and defines `GET /health`.
Once `routes/slots.py` is ready, add these two lines to `app.py`:

```python
from routes.slots import slots_bp
```

and:

```python
app.register_blueprint(slots_bp)
```

Do not duplicate `/health` or create a second Flask `app` instance.

---

## Important Implementation Notes (From Specification)

1. **MySQL Data Types:** `DATE` columns return `datetime.date` (use `.isoformat()` for `YYYY-MM-DD`) and `TIME` columns return `datetime.timedelta` (convert using `(datetime.min + start_time).strftime('%H:%M')`).
2. **Commits:** Always call `conn.commit()` after `UPDATE` statements.
3. **Safe Reservation:** Reserve in a single atomic `UPDATE` (`WHERE slot_id = %s AND status = 'AVAILABLE'`) and check `cursor.rowcount == 0` to distinguish `404` vs `409`.
4. **Error Format:** Return JSON errors matching the project format:
   ```json
   {"error": {"code": "SLOT_NOT_AVAILABLE", "message": "Slot 12 is already booked"}}
   ```

---

## Git Workflow

1. Pull the latest changes (or branch off `feature/person2-doctor-management` once merged into `main`).
2. Work on your own feature branch (for example, `feature/person3-slot-management`).
3. Only add `routes/slots.py` and register `slots_bp` in `app.py` to avoid merge conflicts.
4. Open a Pull Request when your endpoints are tested and ready.
