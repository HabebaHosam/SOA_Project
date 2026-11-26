# pyrefly: ignore[missing-import]
import mysql.connector
import config


def get_connection():
    """Return a new MySQL connection using config credentials."""
    return mysql.connector.connect(
        host=config.DB_HOST,
        port=config.DB_PORT,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD
    )
