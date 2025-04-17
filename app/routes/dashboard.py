from flask import Blueprint

dashboard_bp = Blueprint('dashboard', __name__, url_prefix="/dashboard")


@dashboard_bp.route('/', methods=['GET'])
def dashboard():
    return "Welcome to the Dashboard!"
