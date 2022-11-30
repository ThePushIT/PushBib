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

    signup_success = user_service.register(username, password, password_again)
    if signup_success[0] == True:
        return render_template("success.html", message="Käyttäjätunnus luotu")
    else:
        return render_template("signup.html", message=signup_success[1])
