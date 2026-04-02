from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "ACEest DevOps Application v3"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    name = data.get("name")
    program = data.get("program")

    return jsonify({
        "message": f"Plan generated for {name}",
        "program": program
    })

if __name__ == "__main__":
    app.run(debug=True)