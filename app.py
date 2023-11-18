import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_stock")
def get_stock():
    print("Reached the get_stock route")
    stock = mongo.db.stock.find()
    return render_template("stock.html", stock=stock)
  
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

        # Redirect to a different endpoint, for example, the login page
        return redirect(url_for("login"))

    # For the "GET" request, render the register.html template
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
   
    if user and check_password_hash(user.password, password):
        # Valid credentials, return user information or generate a token
        return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
    else:
        # Invalid credentials
        return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)