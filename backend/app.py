from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Plant Health Scanner API Running"

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['image']

    # Dummy logic (we'll improve later)
    result = "Healthy"

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)