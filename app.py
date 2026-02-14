import os
import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Railway or Local connection
if "MYSQLHOST" in os.environ:
    conn = mysql.connector.connect(
        host=os.environ.get("MYSQLHOST"),
        user=os.environ.get("MYSQLUSER"),
        password=os.environ.get("MYSQLPASSWORD"),
        database=os.environ.get("MYSQLDATABASE"),
        port=int(os.environ.get("MYSQLPORT"))
    )
else:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Tangirala@2026",
        database="shopdb"
    )

cursor = conn.cursor()


@app.route("/")
def home():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return render_template("index.html", products=products)


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


if __name__ == "__main__":
    app.run()
