from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# -------------------------------
# MongoDB Atlas Configuration
# -------------------------------
# Replace with your actual connection string
client = MongoClient("mongodb+srv://:@devops.s1bdw1x.mongodb.net/?appName=Devops")
db = client["todo_db"]
collection = db["items"]

# -------------------------------
# API Route (Reads from JSON file)
# -------------------------------
@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open('backend_data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -------------------------------
# Frontend Form Page
# -------------------------------
@app.route('/')
def home():
    return render_template('form.html')

# -------------------------------
# Form Submission (MongoDB Insert)
# -------------------------------
@app.route('/submit', methods=['POST'])
def submit():
    try:
        item_name = request.form.get('itemName')
        item_desc = request.form.get('itemDescription')

        if not item_name or not item_desc:
            return render_template('form.html', error="All fields are required")

        collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_desc
        })

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('form.html', error=str(e))

# -------------------------------
# Success Page
# -------------------------------
@app.route('/success')
def success():
    return "Data submitted successfully"

# -------------------------------
# Run App
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)