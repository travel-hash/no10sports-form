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

        url = "https://script.google.com/macros/s/AKfycbwWi_D0ruVLsf7F1IIR6e1jIMxgbg9Lcx_L0rYncuLTTTMmPt1ZxnnPNtR7YehOjopo4g/exec"

        response = requests.post(url, json=data, timeout=5)

        return jsonify({
            "status": "success",
            "google_response": response.text
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
