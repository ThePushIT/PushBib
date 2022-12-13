from flask import render_template, Blueprint, request, redirect
from flask_babel import gettext
from services.user_service import user_service

user_controller = Blueprint("user", __name__)

@user_controller.route("/")
def front_page():
    user_id = user_service.get_id()
    if user_id != 0:
        return redirect("/references")

    return render_template("index.html", page="login")

@user_controller.route("/signup", methods=["GET", "POST"])
def signup():
    page = "signup"
    if request.method == "GET":
        return render_template("signup.html", page=page)

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password_again = request.form["password_again"]

        if password != password_again:
            message_text = gettext("Passwords do not match.")
            return render_template("signup.html", message=message_text, page=page)
        if len(username) < 5 or len(username) > 25:
            message_text = gettext("Username length must be 5-25 characters.")
            return render_template("signup.html", message=message_text, page=page)
        if len(password) < 8 or len(password) > 25:
            message_text = gettext("Password length must be 8-25 characters.")
            return render_template("signup.html", message=message_text, page=page)

    # Onnistunut käyttäjätilin luonti
    if user_service.register(username, password):
        return redirect("/references/")

    message_text = gettext("Username already reserved.")
    return render_template("signup.html", message=message_text, page=page)


@user_controller.route("/login", methods=["POST", "GET"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Onnistunut kirjautuminen
    if user_service.login(username, password):
        return redirect("/references/")

    message_text = gettext("Wrong username or password.")
    return render_template("index.html", message=message_text, page="login")

@user_controller.route("/signout")
def sign_out():
    user_service.logout()
    return redirect("/")
