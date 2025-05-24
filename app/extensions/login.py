from flask_login import LoginManager
from flask import Flask


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from app.extensions.alchemy import alchemy
    from app.models import User
    return alchemy.session.get(User, int(user_id))


def extension_login(app: Flask):
    from app.extensions.alchemy import alchemy
    from app.models import User

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    with app.app_context():
        alchemy.create_all()

        if not User.query.filter_by(username='admin').first():
            admin_user = User(username='admin', email='test@example.com')
            admin_user.set_password('password')
            alchemy.session.add(admin_user)
            alchemy.session.commit()
