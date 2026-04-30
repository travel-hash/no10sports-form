from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

FILE = 'data.csv'

# Create CSV file if it does not exist
if not os.path.exists(FILE):
    with open(FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Phone', 'Email'])

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form submit route
@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()

        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')

        # Save data into CSV
        with open(FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, phone, email])

        return jsonify({"status": "success"})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"status": "error"})

# Run app (IMPORTANT for Render)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
