from flask_sqlalchemy import SQLAlchemy
import os

alchemy = SQLAlchemy()

def extension_alchemy(app):
    
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config['SQLALCHEMY_ECHO'] = True
    app.config["SQLALCHEMY_RECORD_QUERIES"] = True

    alchemy.init_app(app)

    with app.app_context():
        alchemy.create_all()


