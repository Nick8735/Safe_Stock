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

@app.route("/issue_stock/<stock_id>", methods=["POST"])
def delete_stock(stock_id):
    if request.method == "POST":
        # Assuming stock_id is the ObjectId of the document you want to delete
        result = mongo.db.stock.delete_one({"_id": ObjectId(stock_id)})

        if result.deleted_count == 1:
            flash("Stock Successfully Issued")
            # Redirect to the "Issue Stock" page with the specific stock_id
            return redirect(url_for("issue_stock", stock_id=stock_id))
        else:
            flash("Stock not found or issue failed")

        return redirect(url_for("issue_stock"))  # Redirect to stock overview if something goes wrong
    else:
        # Handle GET requests or other methods as needed
        return jsonify({"error": "Method not allowed"}), 405

@app.route("/issue_stock/<stock_id>")
def issue_stock(stock_id):
    # Retrieve the specific stock data
    stock_data = mongo.db.stock.find_one({"_id": ObjectId(stock_id)})

    if stock_data:
        # Render the "Issue Stock" (transaction) page with the specific stock data
        return render_template("issue_stock.html", stock_data=stock_data)
    else:
        # Handle the case where the stock is not found
        flash("Stock not found")
        return redirect(url_for("issue_stock"))

@app.route("/issue_stock/<stock_id>/issue_form", methods=["GET", "POST"])
def issue_form(stock_id):
    if request.method == "POST":
        # Process the form submission and update the stock item
        # You can add code here to update the stock status or perform any other actions

        flash("Stock Successfully Issued")
        return redirect(url_for("issue_stock", stock_id=stock_id))

    # Retrieve the specific stock data for the form
    stock_data = mongo.db.stock.find_one({"_id": ObjectId(stock_id)})

    if stock_data:
        # Render the "Issue Stock" (transaction) form with the specific stock data
        return render_template("issue_form.html", stock_data=stock_data)
    else:
        # Handle the case where the stock is not found
        flash("Stock not found")
        return redirect(url_for("stock_overview"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)

