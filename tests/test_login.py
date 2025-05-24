from flask.testing import FlaskClient


def test_login_status_ok(client: FlaskClient):
    response = client.get('/login')
    assert response.status_code == 200


def test_login_render_title(client: FlaskClient):
    response = client.get('/login')
    html = response.data.decode('utf-8')
    assert '<h3 class="card-title text-black mb-4">Inicio de Sesión</h3>' in html, "Debe contener el título 'Inicio de Sesión'"


def test_login_form_fields(client: FlaskClient):
    response = client.get('/login')
    html = response.data.decode('utf-8')
    assert 'name="username"' in html, "El campo 'username' no está en el formulario"
    assert 'name="password"' in html, "El campo 'password' no está en el formulario"
    assert 'name="submit"' in html,   "El campo 'submit'   no está en el formulario"


def test_login_form_validations(client: FlaskClient):
    response = client.post('/login', data={
        'username': '',
        'password': ''
    })
    html = response.data.decode('utf-8')
    assert 'invalid-feedback' in html, "Los campos deben ser validados"


def test_login_success(client: FlaskClient):
    response = client.post('/login', data={
        'username': 'admin',
        'password': 'password'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == '/dashboard/'


def test_logout_success(logged_client: FlaskClient):
    response = logged_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert response.request.path == '/login', "El usuario debe ser capaz de cerrar su sesión"
