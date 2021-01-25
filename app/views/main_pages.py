from flask import Blueprint, render_template

main_pages = Blueprint('main_pages', __name__)


@main_pages.route("/")
def index():
    """Home view to render all users from database"""
    return render_template("users/users.html")

