from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
   
    load_dotenv()

    app = Flask(__name__)
    
    app.config['DEBUG'] = eval(os.getenv("MODE_DEBUG"))
    
    return app