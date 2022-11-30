from flask import render_template, Blueprint, request, redirect, session
from services.user_service import user_service

user_controller = Blueprint("user", __name__)

@user_controller.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password_again = request.form["password_again"]

        if password != password_again:
            return render_template("register.html", message="Salasanat eroavat")
        elif len(username) < 5:
            return render_template("register.html", message="Tunnuksen tulee olla vähintään 5 merkkiä pitkä")
        elif len(password) < 8:
            return render_template("register.html", message="Salasanan tulee olla vähintään 8 merkkiä pitkä")
        elif len(password) > 25 or len(username) > 25:
            return render_template("register.html", message="Käyttäjätunnus ja/tai salasana on liian pitkä")

    #Onnistunut käyttäjätilin luonti
    if user_service.register(username, password):
        return redirect("/references/" + str(user_service.get_id()))
    else:
        return render_template("signup.html", message="Käyttäjätunnus on jo käytössä")


@user_controller.route("/login", methods=["POST", "GET"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    #Onnistunut kirjautuminen
    if user_service.login(username, password):
        return redirect("/references/" + str(user_service.get_id()))
    else:
        return render_template("success.html", message="Väärä käyttäjätunnus tai salasana")
