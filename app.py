import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

# Railway MySQL connection
db = mysql.connector.connect(
    host=os.getenv("MYSQLHOST"),
    port=os.getenv("MYSQLPORT"),
    user=os.getenv("MYSQLUSER"),
    password=os.getenv("MYSQLPASSWORD"),
    database=os.getenv("MYSQLDATABASE")
)

@app.route("/")
def home():
    return "Shop app is running successfully 🚀"

@app.route("/testdb")
def testdb():
    cursor = db.cursor()
    cursor.execute("SELECT DATABASE();")
    result = cursor.fetchone()
    return f"Connected to database: {result}"

if __name__ == "__main__":
    app.run()
