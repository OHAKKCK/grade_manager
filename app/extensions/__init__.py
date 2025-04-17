from .alchemy import extension_alchemy


def register_extensions(app):
    extension_alchemy(app)
