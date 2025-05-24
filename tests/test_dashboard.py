from flask.testing import FlaskClient


def test_dashboard_protected(client: FlaskClient):
    response = client.get('/dashboard/')
    assert response.status_code == 302


def test_dashboard_render(logged_client: FlaskClient):
    response = logged_client.get('/dashboard/')
    assert response.status_code == 200
    assert b'Hello World' in response.data
