from flask import Flask, jsonify
import config
from routes.doctors import doctors_bp

app = Flask(__name__)
app.register_blueprint(doctors_bp)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "service": config.SERVICE_NAME,
        "status": "UP"
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=config.SERVICE_PORT,
        debug=True
    )
