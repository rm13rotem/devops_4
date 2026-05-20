import os
import logging
import subprocess

from flask import Flask, jsonify, request

from apps.JsonSerializer import JsonSerializer
from apps.Machine import Machine


# Create Flask app
app = Flask(__name__)


# Logging configuration
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[
        logging.FileHandler('./logs/log.txt'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# Load machines from file
serializer = JsonSerializer()
machines = serializer.Load()


# Home route
@app.route("/")
def home():

    return jsonify({
        "message": "Machine Manager Flask App Running"
    })


# Health check route
@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


# List all machines
@app.route("/machines", methods=["GET"])
def list_machines():

    return jsonify([
        machine.dict()
        for machine in machines
    ])


# Add machine
@app.route("/machines", methods=["POST"])
def add_machine():

    try:

        data = request.json

        machine = Machine(
            id=data["id"],
            name=data["name"],
            status=data["status"],
            ip=data.get("ip"),
            operating_system=data.get("operating_system", "Linux"),
            cpu_cores=data.get("cpu_cores", 4),
            ram_gb=data.get("ram_gb", 16)
        )

        machines.append(machine)

        serializer.Save(machines)

        logger.info("Machine added successfully")

        return jsonify({
            "message": "Machine added successfully"
        }), 201

    except Exception as ex:

        logger.error(str(ex))

        return jsonify({
            "error": str(ex)
        }), 400


# Run bash script
@app.route("/run-script", methods=["POST"])
def run_script():

    try:

        result = subprocess.run(
            ["bash", "scripts/server.sh"],
            check=True,
            capture_output=True,
            text=True
        )

        logger.info("Script executed successfully")

        return jsonify({
            "output": result.stdout
        })

    except subprocess.CalledProcessError as err:

        logger.error(str(err))

        return jsonify({
            "error": err.stderr
        }), 500

    except FileNotFoundError:

        return jsonify({
            "error": "Script not found"
        }), 404


# Start Flask server
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5001
    )

