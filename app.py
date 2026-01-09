
from flask import Flask, request, jsonify, session, redirect, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db_connection

app = Flask(__name__)
app.secret_key = "secret_key"

# REGISTER
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",
        (data['name'], data['email'],
         generate_password_hash(data['password']))
    )
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "Registered"}), 201

# LOGIN
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email=%s", (data['email'],))
    user = cursor.fetchone()
    cursor.close()
    db.close()

    if user and check_password_hash(user['password'], data['password']):
        session['user_id'] = user['id']
        return jsonify({"message": "Login success"})
    return jsonify({"error": "Invalid"}), 401

# HOME
@app.route('/home')
def home():
    return render_template('home.html')

# ACCOUNT
@app.route('/account')
def account():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "SELECT name,email FROM users WHERE id=%s",
        (session['user_id'],)
    )
    user = cursor.fetchone()
    cursor.close()
    db.close()
    return render_template('account.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)
