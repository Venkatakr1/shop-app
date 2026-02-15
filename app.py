import os
import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Railway MySQL connection
conn = mysql.connector.connect(
    host=os.environ.get("MYSQLHOST"),
    user=os.environ.get("MYSQLUSER"),
    password=os.environ.get("MYSQLPASSWORD"),
    database=os.environ.get("MYSQLDATABASE"),
    port=int(os.environ.get("MYSQLPORT"))
)

cursor = conn.cursor()

# ✅ CREATE TABLE with AUTO_INCREMENT (IMPORTANT)
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price INT,
    quantity INT
)
""")

conn.commit()


# ✅ HOME PAGE
@app.route("/")
def home():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return render_template("index.html", products=products)


# ✅ ADD PRODUCT
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    price = request.form["price"]
    quantity = request.form["quantity"]

    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)",
        (name, price, quantity)
    )

    conn.commit()

    return redirect("/")


# ✅ RUN APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
