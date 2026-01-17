from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="userdb"
)

cursor = db.cursor()

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        val = (username, email, password)
        cursor.execute(sql, val)
        db.commit()

        return "User Registered Successfully!"

    return render_template("register.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

