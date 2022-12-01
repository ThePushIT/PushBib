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
            message_text = "Salasanat eroavat"
            return render_template("signup.html", message=message_text)
        if len(username) < 5:
            message_text = "Tunnuksen tulee olla vähintään 5 merkkiä pitkä"
            return render_template("signup", message=message_text)
        if len(password) < 8:
            message_text = "Salasanan tulee olla vähintään 8 merkkiä pitkä"
            return render_template("signup.html", message=message_text)
        if len(password) > 25 or len(username) > 25:
            message_text = "Käyttäjätunnus ja/tai salasana on liian pitkä"
            return render_template("signup.html", message=message_text)

    # Onnistunut käyttäjätilin luonti
    if user_service.register(username, password):
        return redirect("/references/" + str(user_service.get_id()))

    return render_template("signup.html", message="Käyttäjätunnus on jo käytössä")


@user_controller.route("/login", methods=["POST", "GET"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Onnistunut kirjautuminen
    if user_service.login(username, password):
        return redirect("/references/" + str(user_service.get_id()))

    return render_template("index.html", message="Väärä käyttäjätunnus tai salasana")
