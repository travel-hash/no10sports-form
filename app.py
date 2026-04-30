from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

FILE = 'data.csv'

# Create CSV if not exists
if not os.path.exists(FILE):
    with open(FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Phone', 'Email'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()

        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')

        # Save data (NO duplicate check)
        with open(FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, phone, email])

        return jsonify({"status": "success"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run()
