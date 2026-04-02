import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

programs = ["Fat Loss", "Muscle Gain", "Beginner"]


def init_db():
    conn = sqlite3.connect("aceest.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS clients (name TEXT, program TEXT)")
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return "ACEest DevOps Application v4"

@app.route("/members")
def members():
    return jsonify({
        "members": ["Ramesh", "Suresh", "Mahesh", "John"]
    })

@app.route("/programs")
def get_programs():
    return jsonify({"programs": programs})

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    return jsonify({"message": "Plan generated"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)