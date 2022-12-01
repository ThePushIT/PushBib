from flask import render_template, Blueprint, request, redirect
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
            message_text = "Passwords do not match"
            return render_template("signup.html", message=message_text)
        if len(username) < 5:
            message_text = "Username must be at least 5 characters."
            return render_template("signup.html", message=message_text)
        if len(password) < 8:
            message_text = "Password must be at least 8 characters."
            return render_template("signup.html", message=message_text)
        if len(password) > 25 or len(username) > 25:
            message_text = "Username or password is too long"
            return render_template("signup.html", message=message_text)

    # Onnistunut käyttäjätilin luonti
    if user_service.register(username, password):
        return redirect("/references/" + str(user_service.get_id()))

    return render_template("signup.html", message="Username already reserved")


@user_controller.route("/login", methods=["POST", "GET"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Onnistunut kirjautuminen
    if user_service.login(username, password):
        return redirect("/references/" + str(user_service.get_id()))

    return render_template("index.html", message="Wrong username or password")
