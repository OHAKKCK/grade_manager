from flask import request
from flask_login import current_user


def inject_user():
    url_prefix = request.path.split("/")[1]
    return dict(
        current_user=current_user,
        actual_route=request.path,
        url_prefix=url_prefix
    )
