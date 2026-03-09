from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ACEest DevOps Application"

@app.route("/members")
def members():
    return jsonify({
        "members": [
            "Ramesh",
            "Suresh",
            "Mahesh"
            "John"
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)