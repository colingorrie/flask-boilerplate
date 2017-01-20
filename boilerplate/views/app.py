from flask import Blueprint, render_template


app_blueprint = Blueprint("blueprint", __name__)


@app_blueprint.route("/", defaults={"path": ""})
@app_blueprint.route("/<path:path>")
def catch_all(path):
    return render_template("app/root.html")
