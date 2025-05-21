from flask import Flask
from dotenv import load_dotenv
from app.routes import register_routes
from app.extensions import register_extensions
import os

def create_app():
   
    load_dotenv(override=True)

    app = Flask(__name__)
    
    app.config['DEBUG'] = eval(os.getenv("MODE_DEBUG"))
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

    register_routes(app)
    register_extensions(app)

    return app