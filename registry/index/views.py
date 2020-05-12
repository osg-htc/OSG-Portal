from flask import Blueprint, request, current_app, make_response, render_template

index_bp = Blueprint(
    "index",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/index",
)


@index_bp.route("/")
def index():
    return make_response(render_template("index.html"))


@index_bp.route("/health")
def health():
    return "Hello!"
