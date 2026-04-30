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

        response = requests.post(url, data=data)

        if response.status_code != 200:
            return jsonify({"status": "error", "message": "Failed to send data"})

        return jsonify({"status": "success"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run()
