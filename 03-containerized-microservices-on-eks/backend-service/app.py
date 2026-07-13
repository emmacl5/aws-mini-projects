from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        service="backend-service",
        message="Hello from the backend microservice",
        hostname=socket.gethostname(),
    ), 200


@app.get("/api/message")
def get_message():
    return jsonify(
        service="backend-service",
        message="The backend service is running successfully",
        environment=os.getenv("APP_ENV", "development"),
        hostname=socket.gethostname(),
    ), 200


@app.get("/health")
def health():
    return jsonify(
        status="healthy",
        service="backend-service",
    ), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5001"))
    app.run(host="0.0.0.0", port=port)
