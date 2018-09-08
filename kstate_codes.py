from flask import Blueprint, render_template

codes = Blueprint('kstatecodes', __name__)


@codes.route('/')
def hello_world():
    return render_template("home.html")


