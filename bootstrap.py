from flask import Flask
from dotenv import load_dotenv
from app.routes import register_routes
from app.extensions import register_extensions
from app.context import inject_user
import os

def create_app():
   
    load_dotenv(override=True)

    app = Flask(__name__)
    
    app.config['DEBUG'] = eval(os.getenv("MODE_DEBUG"))
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

    register_routes(app)
    register_extensions(app)

    app.context_processor(inject_user)

    return app