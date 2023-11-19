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
app.static_folder = 'static'

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
def index():
    return redirect(url_for("login"))

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
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("get_stock"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/stock-overview")
def stock_overview():
    print("Reached the stock_overview route")
    
    # Retrieve data from MongoDB
    stock_data = mongo.db.stock.find()
    
    # Pass data to template
    return render_template("stock-list.html", stock_data=stock_data)

@app.route("/receipt", methods=["GET"])
def receipt():
    return render_template("receipt.html")

@app.route("/receipt_form", methods=["POST"])
def receipt_form():
    # Get data from the form
    key1_value = request.form.get("key1")
    key2_value = request.form.get("key2")

    # Create a dictionary representing the document
    data = {"key1": key1_value, "key2": key2_value}

    # Insert the document into the MongoDB collection
    result = mongo.db.collection_name.insert_one(data)

    # Check if the insertion was successful
    if result.acknowledged:
        return "Document inserted successfully!"
    else:
        return "Failed to insert document."

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
