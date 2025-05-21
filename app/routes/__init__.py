from .dashboard import dashboard_bp
from .students import students_bp

def register_routes(app):
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(students_bp)