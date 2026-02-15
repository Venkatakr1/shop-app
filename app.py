import os
import mysql.connector
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("MYSQLHOST"),
        user=os.environ.get("MYSQLUSER"),
        password=os.environ.get("MYSQLPASSWORD"),
        database=os.environ.get("MYSQLDATABASE"),
        port=int(os.environ.get("MYSQLPORT"))
    )


@app.route("/")
def home():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, price, quantity FROM products")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", products=products)


@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    price = request.form["price"]
    quantity = request.form["quantity"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products (id, name, price, quantity) VALUES (NULL, %s, %s, %s)",
        (name, price, quantity)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")
@app.route("/delete/<int:id>")
def delete(id):
    cursor.execute("DELETE FROM products WHERE id = %s", (id,))
    conn.commit()
    return redirect("/")



if __name__ == "__main__":
    app.run()
