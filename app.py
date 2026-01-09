from flask import Flask, request, jsonify, session
from werkzeug.security import check_password_hash
from db import get_db_connection

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, name, email, password FROM users WHERE email=%s",
        (email,)
    )
    user = cursor.fetchone()

    cursor.close()
    db.close()

    if user and check_password_hash(user['password'], password):
        session['user_id'] = user['id']
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user['id'],
                "name": user['name'],
                "email": user['email']
            }
        }), 200

    return jsonify({"error": "Invalid email or password"}), 401

if __name__ == '__main__':
    app.run(debug=True)
