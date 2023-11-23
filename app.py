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

@app.route("/receipt_form", methods=["GET", "POST"])
def receipt_form():
    if request.method == "POST":
        receipt = {
            "stock_name": request.form.get("stock_name"),
            "stock_number": request.form.get("stock_number"),
            "stock_uom": request.form.get("stock_uom"),
            "stock_location": request.form.get("stock_location"),
            "stock_qty": request.form.get("stock_qty"),
            "created_by": session["user"]
        }
        mongo.db.stock.insert_one(receipt)
        flash("Stock Successfully Added")
        return redirect(url_for("receipt_form"))

    return render_template("receipt.html")

@app.route("/issue")
def issue():
    return render_template("issue.html")


@app.route("/issue_form", methods=["GET", "POST"])
def issue_form():
    if request.method == "POST":
        issue = {
            "stock_name": request.form.get("stock_name"),
            "stock_number": request.form.get("stock_number"),
            "stock_uom": request.form.get("stock_uom"),
            "stock_location": request.form.get("stock_location"),
            "stock_qty": request.form.get("stock_qty"),
            "created_by": session["user"]
        }
        
        # Assuming "stock" is the collection in your MongoDB
        mongo.db.stock.delete_one(issue)
        
        flash("Stock Successfully Deleted")

        # Redirect to a different route after successful deletion
        return redirect(url_for("stock_overview"))  # Change "stock_overview" to the appropriate route

    return render_template("issue.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)

