# twitoff/routes/home_routes.py

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def hello_world():
    return render_template("prediction_form.html")
    # return "Hello, World!"

@home_routes.route("/about")
def about():
    print("Oh look. You've managed to get to the home page. Aren't you special")
    return "About Me (TODO)"