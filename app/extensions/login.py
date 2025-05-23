from flask_login import LoginManager
from flask import Flask

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))


def extension_login(app: Flask):
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
