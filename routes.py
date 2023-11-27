from app import app
from flask import render_template, request, redirect, session
import reviews, users, restaurants

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/main")
def main():
    list = restaurants.get_list()
    length = len(list)
    return render_template("main.html", restaurants=list, length=length)

@app.route("/rev_page", methods=["GET","POST"])
def rev_page():
    id = int(request.form.get("selectedOption"))
    list = reviews.get_list(id)
    name = restaurants.get_restaurant(id)
    session["restaurant"] = name[0]
    session["restaurant_id"] = id
    return render_template("list.html", reviews=list)

@app.route("/review", methods=["GET", "POST"])
def review():
    if request.method == "GET":
        return render_template("review.html")
    if request.method == "POST":
        id = session["restaurant_id"]
        rating = request.form.get("rate")
        print(rating)
        content = request.form["content"]
        if reviews.send(id, content, rating):
            return redirect("/main")
        else:
            return render_template("error.html", message="Arvostelun lisäys ei onnistunut")
        
@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "GET":
        return render_template("new.html")
    if request.method == "POST":
        name = request.form["name"]
        longitude = request.form["longitude"]
        latitude = request.form["latitude"]
        if restaurants.add_restaurant(name, longitude, latitude):
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