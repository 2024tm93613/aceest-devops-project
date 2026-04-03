from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (simple for now)
program_list = ["Yoga", "Cardio", "Strength Training"]

program_details = {
    "Yoga": "Flexibility and relaxation",
    "Cardio": "Heart and endurance training",
    "Strength Training": "Muscle building"
}

@app.route("/")
def home():
    return "Hello World"

@app.route("/members")
def members():
    return jsonify({"members": ["A", "B", "C"]})

# GET all programs
@app.route("/programs", methods=["GET"])
def programs():
    return jsonify({"programs": program_list})

# GET program by name
@app.route("/programs/<name>", methods=["GET"])
def program_detail(name):
    return jsonify({
        "program": name,
        "description": program_details.get(name, "Program not found")
    })

# ✅ NEW: POST program
@app.route("/programs", methods=["POST"])
def add_program():
    data = request.get_json()

    name = data.get("name")
    description = data.get("description")

    if not name or not description:
        return jsonify({"error": "Invalid input"}), 400

    program_list.append(name)
    program_details[name] = description

    return jsonify({
        "message": "Program added successfully",
        "program": name
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)