from flask import Flask, jsonify, request

app = Flask(__name__)

programs = ["Fat Loss", "Muscle Gain", "Beginner"]

@app.route("/")
def home():
    return "ACEest DevOps Application v3"

@app.route("/members")
def members():
    return jsonify({
        "members": ["Ramesh", "Suresh", "Mahesh", "John"]
    })

@app.route("/programs")
def get_programs():
    return jsonify({"programs": programs})

# NEW
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    name = data.get("name")
    program = data.get("program")

    if not name or not program:
        return jsonify({"error": "Missing fields"}), 400

    return jsonify({
        "message": f"Plan generated for {name}",
        "program": program
    })

if __name__ == "__main__":
    app.run(debug=True)