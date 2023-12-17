from app import app
from flask import render_template, request, redirect, session
import reviews, users, restaurants

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/main")
def main():
    restaurant_list = restaurants.get_list()
    raw_list = restaurants.get_review_data()
    review_list = []
    for name, category, rating, count in raw_list:
        if rating is not None:
            rating = round(rating,1)
        else:
            rating = "Ei arvosteluja"
        review_list.append((name,category,rating, count))
    review_list = sorted(review_list, key=lambda x: x[2], reverse=True)
    length = len(restaurant_list)
    return render_template("main.html", restaurants=restaurant_list, reviews=review_list, length=length)

@app.route("/rev_page", methods=["GET","POST"])
def rev_page():
    if request.method == "POST":
        name = request.form.get("chosen_option")
        id = restaurants.get_restaurant_id(name)
        id = id[0]
        session["restaurant_id"] = id
    if request.method == "GET":
        id = session["restaurant_id"]
    rev_list = reviews.get_list(id)
    res_data = restaurants.get_restaurant_data(id)
    avg_rating = reviews.get_avg_rating(id)
    avg_rating = avg_rating[0]
    if avg_rating is None:
        avg_rating = 0
    name = restaurants.get_restaurant_name(id)
    session["restaurant"] = name[0]
    return render_template("list.html", reviews=rev_list, data=res_data, rating=avg_rating, count=len(rev_list))

@app.route("/review", methods=["GET", "POST"])
def review():
    if request.method == "GET":
        return render_template("review.html")
    if request.method == "POST":
        id = session["restaurant_id"]
        rating = request.form.get("rate")
        content = request.form["content"]
        if len(content) > 5000:
            return render_template("error.html", message="Arvostelun sisältö on liian pitkä")
        if reviews.send(id, content, rating):
            return redirect("/rev_page")
        else:
            return render_template("error.html", message="Arvostelun lisäys ei onnistunut")
        
@app.route("/new", methods=["GET", "POST"])
def new():
    categories = ["Fine dining", "Pikaruokala", "Etninen", "Pizzeria", "Kahvila", "Pubi"]
    if request.method == "GET":
        return render_template("new.html", categories=categories)
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["content"]
        if len(description) > 5000:
            return render_template("error.html", message="Ravintolan kuvaus on liian pitkä")
        address = request.form["address"]
        hours = request.form["hours"]
        category = request.form.get("selectedOption")
        if restaurants.add_restaurant(name, description, address, hours, category):
            return redirect("/main")
        else:
            return render_template("error.html", message="Ravintolan lisäys ei onnistunut")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/main")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        

@app.route("/delete_review", methods=["POST"])
def delete_review():
    if request.method == "POST":
        id = request.form["id"]
        reviews.delete_review(id)
        return redirect("/rev_page")
    

@app.route("/delete_restaurant", methods=["POST"])
def delete_restaurant():
    if request.method == "POST":
        id = request.form["id"]
        restaurants.delete_restaurant(id)
        return redirect("/main")
    
@app.route("/add_admin", methods=["POST"])
def add_admin():
    if request.method == "POST":
        id = request.form["id"]
        users.add_admin(id)
        return redirect("/user_list")
    

@app.route("/user_list", methods=["GET","POST"])
def user_list():
    user_list = users.get_list()
    if request.method == "GET":
        return render_template("users.html", user_list=user_list)
