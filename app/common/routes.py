from flask import Blueprint, render_template

main = Blueprint('main', __name__, url_prefix='')


@main.route("/")
def index():
    return render_template("index.html")

@main.route("/clientside_table")
def clientside_table():
    return render_template("clientside_table.html")

@main.route("/serverside_table")
def serverside_table():
    return render_template("serverside_table.html")
