import socket
import json
import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

HOSTNAME = socket.gethostname()
# IP_ADDRESS = socket.gethostbyname(HOSTNAME)
IP_ADDRESS = socket.getaddrinfo(HOSTNAME)
RECEIVER_URL = os.getenv("RECEIVER_URL", "http://receiver:8000/report")
PORT_RANGE = range(20, 1025)

logging.basicConfig(level=logging.INFO)


def scan_ports():
    open_ports = []
    for port in PORT_RANGE:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex(("127.0.0.1", port))
            if result == 0:
                open_ports.append(port)
    return open_ports


def report():
    ports = scan_ports()
    data = {
        "hostname": HOSTNAME,
        "ip": IP_ADDRESS,
        "open_ports": ports
    }
    try:
        res = requests.post(RECEIVER_URL, json=data)
        logging.info(f"Reported to receiver: {res.status_code}")
    except Exception as e:
        logging.error(f"Failed to report: {e}")


if __name__ == "__main__":
    report()
