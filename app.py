from flask import Flask, render_template, request, jsonify
import csv, os

app = Flask(__name__)

FILE = 'data.csv'

# ensure file exists
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
        data = request.get_json(force=True)

        name = data.get('name', '')
        phone = data.get('phone', '')
        email = data.get('email', '')

        with open(FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, phone, email])

        return jsonify({"status": "success"})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"status": "error"})

# IMPORTANT FOR RENDER
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
