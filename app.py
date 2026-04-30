from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()

        url = "https://script.google.com/macros/s/AKfycbyvWrONX0Kk1foAdLtqjsOMatlKE6nMQUuPH8SM-STHRV0BQYOCai-vnbPowLshfhHmMg/exec"

        # SAFE REQUEST (IMPORTANT)
        response = requests.post(url, data=data, timeout=5)

        return jsonify({
            "status": "success",
            "google_response": response.text
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

# VERY IMPORTANT FOR RENDER
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
