from flask import Flask, request, render_template
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.environ.get("34.93.87.205"),
    user=os.environ.get("myuser"),
    password=os.environ.get("myjawhar"),
    database=os.environ.get("myappdb2")
)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['GET'])
def submit():
    name = request.args.get("name")
    if not name:
        return "Please provide a name in form"
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    db.commit()
    return f"Name {name} added to Cloud SQL!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
