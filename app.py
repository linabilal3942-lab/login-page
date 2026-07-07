from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL",
    "sqlite:///users.db"
)

db = SQLAlchemy(app)


# User Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


# Create database and default user
with app.app_context():
    db.create_all()

    if not User.query.filter_by(username="admin").first():
        user = User(
            username="admin",
            password=generate_password_hash("1234")
        )
        db.session.add(user)
        db.session.commit()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return jsonify({
            "success": True,
            "message": "Login Successful!"
        })

    return jsonify({
        "success": False,
        "message": "Username or Password is incorrect!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)