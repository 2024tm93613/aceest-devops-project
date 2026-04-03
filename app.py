from flask import Flask, jsonify, request
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# ✅ define empty list
members_list = []
programs = ["Yoga", "Cardio", "Strength"]
program_details = {
    "Yoga": "Flexibility",
    "Cardio": "Endurance",
    "Strength": "Muscle building"
}

@app.route("/")
def home():
    logging.info("Home endpoint called")
    return "Welcome to ACEest Fitness & Gym"

@app.route("/members")
def members():
    return jsonify({"members": members_list})

@app.route("/programs")
def get_programs():
    return jsonify({"programs": programs})

@app.route("/programs/<name>")
def get_program(name):
    if name not in program_details:
        return {"error": "Program not found"}, 404

    return {
        "program": name,
        "description": program_details[name]
    }

@app.route("/programs", methods=["POST"])
def add_program():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name")

    if not name:
        return jsonify({"error": "Invalid input"}), 400


    if not name:
        return {"error": "Invalid input"}, 400
    
    if name in programs:
        return {"error": "Program exists"}, 409

    programs.append(name)

    return {"message": "Program added"}, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)