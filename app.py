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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)