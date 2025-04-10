from flask import Flask, request, jsonify
import json
import os
import logging

app = Flask(__name__)
LOG_FILE = os.getenv("LOG_FILE", "data.json")

logging.basicConfig(level=logging.INFO)


def save_report(data):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            existing = json.load(f)
    else:
        existing = []
    existing.append(data)
    with open(LOG_FILE, "w") as f:
        json.dump(existing, f, indent=2)


@app.route("/report", methods=["POST"])
def receive_report():
    data = request.json
    logging.info(f"Received data: {data}")
    save_report(data)
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
