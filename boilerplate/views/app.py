from flask import Blueprint, render_template


app_blueprint = Blueprint("blueprint", __name__)


@app_blueprint.route("/")
def root():
    return render_template("app/root.html")
