import pytest
from bootstrap import create_app


@pytest.fixture()
def app():
    flask_app = create_app()
    flask_app.config['TESTING'] = True
    flask_app.config['WTF_CSRF_ENABLED'] = False
    yield flask_app


@pytest.fixture()
def client(app):
    yield app.test_client()


@pytest.fixture
def logged_client(client):
    client.post('/login', data={
        'username': 'admin',
        'password': 'password'
    }, follow_redirects=True)
    yield client

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()