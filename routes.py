from app import app
from flask import render_template, request, redirect
import reviews, users, restaurants

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/main")
def main():
    list = restaurants.get_list()
    length = len(list)
    return render_template("main.html", restaurants=list, length=length)

@app.route("/list", methods=["GET","POST"])
def list():
    selected_option = request.form.get("selectedOption")
    list = reviews.get_list(selected_option)
    return render_template("list.html", reviews=list)

@app.route("/review", methods=["GET", "POST"])
def review():
    if request.method == "GET":
        return render_template("review.html")
    if request.method == "POST":
        id = request.form["id"]
        rating = request.form["rating"]
        content = request.form["content"]
        print(rating)
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