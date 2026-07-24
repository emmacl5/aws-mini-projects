import os
import socket

import requests
from flask import Flask, jsonify

app = Flask(__name__)

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:5001",
)


@app.get("/")
def index():
    return jsonify(
        service="frontend-service",
        message="Frontend microservice is running",
        hostname=socket.gethostname(),
        backend_url=BACKEND_URL,
    ), 200


@app.get("/api")
def call_backend():
    try:
        response = requests.get(
            f"{BACKEND_URL}/api/message",
            timeout=5,
        )
        response.raise_for_status()

        return jsonify(
            service="frontend-service",
            message="Successfully received a response from the backend",
            frontend_hostname=socket.gethostname(),
            backend_response=response.json(),
        ), 200

    except requests.exceptions.Timeout:
        return jsonify(
            service="frontend-service",
            error="The backend service timed out",
            backend_url=BACKEND_URL,
        ), 504

    except requests.exceptions.ConnectionError:
        return jsonify(
            service="frontend-service",
            error="Unable to connect to the backend service",
            backend_url=BACKEND_URL,
        ), 503

    except requests.exceptions.HTTPError as error:
        return jsonify(
            service="frontend-service",
            error="The backend returned an HTTP error",
            details=str(error),
        ), 502

    except requests.exceptions.RequestException as error:
        return jsonify(
            service="frontend-service",
            error="An unexpected backend request error occurred",
            details=str(error),
        ), 500


@app.get("/health")
def health():
    return jsonify(
        status="healthy",
        service="frontend-service",
    ), 200


@app.get("/ready")
def readiness():
    try:
        response = requests.get(
            f"{BACKEND_URL}/health",
            timeout=3,
        )
        response.raise_for_status()

        return jsonify(
            status="ready",
            service="frontend-service",
            backend_status=response.json(),
        ), 200

    except requests.exceptions.RequestException:
        return jsonify(
            status="not ready",
            service="frontend-service",
            reason="Backend service is unavailable",
        ), 503


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
