from flask import Flask, jsonify

app = Flask(__name__)

# ✅ define empty list
members_list = []

@app.route("/")
def home():
    return "Welcome to ACEest Fitness & Gym"

@app.route("/members")
def members():
    return jsonify({"members": members_list})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)