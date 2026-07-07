from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ለምሳሌ ብቻ (Database በኋላ እንጨምራለን)
USER = {
    "username": "admin",
    "password": "1234"
}

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Login API
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == USER["username"] and password == USER["password"]:
        return jsonify({
            "success": True,
            "message": "Login Successful!"
        })

    return jsonify({
        "success": False,
        "message": "Username or Password is incorrect!"
    })


if __name__ == "__main__":
    app.run(debug=True)