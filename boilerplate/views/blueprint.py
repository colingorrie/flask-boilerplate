from flask import Blueprint, render_template


blueprint = Blueprint("blueprint", __name__)


@blueprint.route("/")
def root():
    return render_template("blueprint/root.html")
