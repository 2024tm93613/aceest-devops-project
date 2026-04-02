from flask import Flask, jsonify

app = Flask(__name__)

programs = ["Fat Loss", "Muscle Gain", "Beginner"]

@app.route("/")
def home():
    return "ACEest DevOps Application v2"

@app.route("/members")
def members():
    return jsonify({"members": ["Ramesh", "Suresh", "Mahesh", "John"]})

# NEW
@app.route("/programs")
def get_programs():
    return jsonify({"programs": programs})

if __name__ == "__main__":
    app.run(debug=True)