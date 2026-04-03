from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ACEest DevOps Application - Version-1"

@app.route("/members")
def members():
    return jsonify({
        "members": [
            "Ramesh",
            "Suresh",
            "Mahesh",
            "John",
            "Mohan"
        ]
    })

@app.route("/programs")
def programs():
    return jsonify({
        "programs": ["Yoga", "Cardio", "Strength Training"]
    })

# ✅ NEW: Program by name (v2)
@app.route("/programs/<name>")
def program_detail(name):
    data = {
        "Yoga": "Flexibility and relaxation",
        "Cardio": "Heart and endurance training",
        "Strength Training": "Muscle building"
    }
    return jsonify({
        "program": name,
        "description": data.get(name, "Program not found")
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)