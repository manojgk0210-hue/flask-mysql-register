from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from db import get_db_connection

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.json

    name = data.get('name')
    email = data.get('email')
    password = generate_password_hash(data.get('password'))

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password)
        )
        db.commit()
        return jsonify({"message": "User registered successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    finally:
        cursor.close()
        db.close()

if __name__ == '__main__':
    app.run(debug=True)

