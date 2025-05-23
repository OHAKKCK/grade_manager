from .alchemy import extension_alchemy
from .login import extension_login

def register_extensions(app):
    extension_alchemy(app)
    extension_login(app)
