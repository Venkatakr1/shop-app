from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tangirala@2026",
    database="shopdb"
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM sales ORDER BY id DESC")
    data = cursor.fetchall()
    return render_template("index.html", sales=data)

@app.route('/add', methods=['POST'])
def add_sale():
    product = request.form['product']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])

    total = quantity * price

    query = "INSERT INTO sales (product, quantity, price, total) VALUES (%s, %s, %s, %s)"
    values = (product, quantity, price, total)

    cursor.execute(query, values)
    db.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
