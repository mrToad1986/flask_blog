# служебные настройки, настройки импортов и т.д.
# папка содержащая __init__ преобразуется в package
# создаваемое приложение app будет экземпляром класса-конструктора Flask
# подключаем базу данных и аутентификацию

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_blog.config import Config
from flask_bcrypt import Bcrypt
from flask_mail import Mail

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()

def create_app(config_class=Config):
    # print(__name__)

    app = Flask(__name__)
    app.config.from_object(Config)

    from flask_blog.main.routes import main
    app.register_blueprint(main)

    from flask_blog.users.routes import users
    app.register_blueprint(users)

    from flask_blog.posts.routes import posts
    app.register_blueprint(posts)

    from flask_blog.errors.handlers import errors
    app.register_blueprint(errors)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    mail.init_app(app)

    return app