# Blueprint - маршрутизация, контроллер, пространство имен

from flask import render_template, Blueprint
from flask_blog.models import User

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/index.html")
def home():
    return render_template('index.html')

@main.route("/contacts.html")
def contacts():
    return render_template('contacts.html')

@main.route("/blog.html")
def blog():
    return render_template('blog.html')