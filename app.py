import os
import pandas as pd
from bson import Int64 
import plotly.express as px
from flask import jsonify, Flask, flash, render_template, redirect, request, session, url_for
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
    stock = mongo.db.stock.find()
    return render_template("stock.html", stock=stock)

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        print(f"Search Query: {query}")  # Add this line for debugging
        search_results = list(mongo.db.stock.find({"$text": {"$search": query}}))
        print(f"Search Results: {search_results}")  # Add this line for debugging
        return render_template("stock-list.html", search_results=search_results)

    return render_template("stock-list.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("get_stock"))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/stock-overview")
def stock_overview():
    stock_data = mongo.db.stock.find()
    return render_template("stock-list.html", stock_data=stock_data)

@app.route("/stock_check/<stock_id>/edit", methods=["GET"])
def stock_check_edit_page(stock_id):
    stock = mongo.db.stock.find_one({"_id": ObjectId(stock_id)})
    return render_template("stock_check_edit.html", stock=stock)

@app.route("/receipt", methods=["GET"])
def receipt():
    return render_template("receipt.html")

@app.route("/receipt_form", methods=["GET", "POST"])
def receipt_form():
    if request.method == "POST":
        try:
            stock_qty = int(request.form.get("stock_qty"))
        except ValueError:
                
                flash("Invalid quantity. Please enter a valid integer.")
                return redirect(url_for("receipt_form"))

        receipt = {
            "stock_purchase_order": request.form.get("stock_purchase_order"),
            "stock_name": request.form.get("stock_name"),
            "stock_number": request.form.get("stock_number"),
            "stock_uom": request.form.get("stock_uom"),
            "stock_location": request.form.get("stock_location"),
            "stock_qty": stock_qty,
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
            "stock_purchase_order": request.form.get("stock_purchase_order"),
            "stock_name": request.form.get("stock_name"),
            "stock_number": request.form.get("stock_number"),
            "stock_uom": request.form.get("stock_uom"),
            "stock_location": request.form.get("stock_location"),
            "stock_qty": request.form.get("stock_qty"),
            "created_by": session["user"]
        }

        # Construct a filter based on purchase order (adjust criteria as needed)
        filter_criteria = {
            "stock_purchase_order": issue["stock_purchase_order"],
            "stock_name": issue["stock_name"],  # Include other criteria as needed
        }

        # Delete the document that matches the filter
        mongo.db.stock.delete_one(filter_criteria)

        flash("Stock Successfully Issued")
        return redirect(url_for("stock_overview"))

    return render_template("issue.html")

@app.route('/dashboard')
def dashboard():
    stock_data = mongo.db.stock.find()
    df = pd.DataFrame(list(stock_data))

    bar_column_name_x = 'stock_name'
    bar_column_name_y = 'stock_qty'
    bar_fig = px.bar(df, x=bar_column_name_x, y=bar_column_name_y, title='Stock Quantity by Name')

    pie_column_name = 'created_by'
    pie_fig = px.pie(df, names=pie_column_name, title='Users')
    pie_fig.update_traces(marker=dict(colors=['yellow']))

    bar_chart_html = bar_fig.to_html(full_html=False)
    pie_chart_html = pie_fig.to_html(full_html=False)

    return render_template('dashboard.html', bar_chart_html=bar_chart_html, pie_chart_html=pie_chart_html)

@app.route("/stock_check", methods=["GET"])
def stock_check():
    stocks = list(mongo.db.stock.find())
    return render_template("stock_check_view.html", stocks=stocks)

@app.route("/stock_check/<stock_id>", methods=["GET"])
def stock_check_detail(stock_id):
    stock = mongo.db.stock.find_one({"_id": ObjectId(stock_id)})
    return render_template("stock_check_edit.html", stock=stock)

@app.route("/stock_check/<stock_id>/edit", methods=["POST"])
def stock_check_edit(stock_id):
    if request.method == "POST":
        try:
            updated_stock = {
                "stock_purchase_order": request.form.get("stock_purchase_order"),
                "stock_name": request.form.get("stock_name"),
                "stock_number": request.form.get("stock_number"),
                "stock_uom": request.form.get("stock_uom"),
                "stock_location": request.form.get("stock_location"),
                "stock_qty": int(request.form.get("stock_qty")),  # Convert to integer
                "created_by": session["user"]
            }
        except ValueError:
            flash("Invalid quantity. Please enter a valid integer.")
            return redirect(url_for("stock_overview"))

        mongo.db.stock.update_one({"_id": ObjectId(stock_id)}, {"$set": updated_stock})

        flash("Stock Successfully Updated")
        return redirect(url_for("stock_overview"))


@app.route("/stock_count", methods=["GET", "POST"])
def stock_count():
    if request.method == "POST":
        stock_purchase_order = request.form.get("stock_purchase_order")
        stock_name = request.form.get("stock_name")
        stock_number = request.form.get("stock_number")
        stock_uom = request.form.get("stock_uom")
        stock_location = request.form.get("stock_location")
        stock_qty = request.form.get("stock_qty")

        stock = mongo.db.stock.find_one({"stock_name": stock_name})

        if stock:
            differences = []
            if stock["stock_purchase_order"] != stock_purchase_order:
                differences.append("Stock Purchase Order")
            if stock["stock_number"] != stock_number:
                differences.append("Stock Number")
            if stock["stock_uom"] != stock_uom:
                differences.append("Stock UoM")
            if stock["stock_location"] != stock_location:
                differences.append("Stock Location")
            if stock["stock_qty"] != stock_qty:
                differences.append("Stock Quantity")

            if differences:
                flash(f"Incorrect stock count. Differences in: {', '.join(differences)}", "error")
            else:
                flash("Stock count is correct!")
        else:
            flash("Incorrect stock count. Please edit stock at overview.", "error")

    return render_template("stock_count.html")

def get_low_stock_items(threshold_quantity):
    # MongoDB Query: Retrieve items with quantity less than the threshold
    query = {"stock_qty": {"$lt": threshold_quantity}}
    low_stock_items_cursor = mongo.db.stock.find(query)
    
    # Convert the cursor to a list of dictionaries
    low_stock_items = list(low_stock_items_cursor)

    print("Threshold Quantity:", threshold_quantity)
    print("MongoDB Query:", query)
    print("Low Stock Items Count:", len(low_stock_items))
    print("Low Stock Items:", low_stock_items)  # Add this line for debugging

    return low_stock_items


def generate_stock_report_html(low_stock_items):
    # Your HTML content generation logic
    html_content = """
    <html>
    <head>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
                background-color: white;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            h2{
                font-style: oblique;
                text-decoration: underline;
                color: white;
                margin: 50px; 
            }
            th{
                background-color: #ccc;
            }
        </style>
    </head>
    <body>
        <h2>Low Stock Report</h2>
        <table>
            <tr>
                <th>Name</th>
                <th>Quantity</th>
            </tr>
    """

    for item in low_stock_items:
        html_content += f"""
            <tr>
                <td>{item['stock_name']}</td>
                <td>{item['stock_qty']}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """
    return html_content

@app.route("/low_stock")
def low_stock_report():
    # Set your threshold quantity
    threshold_quantity = 6

    # Get low-stock items from MongoDB
    low_stock_items = get_low_stock_items(threshold_quantity)

    # Generate the HTML report
    html_content = generate_stock_report_html(low_stock_items)

    # Render the low_stock.html template and pass the HTML content
    return render_template("low_stock.html", html_content=html_content)

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)

