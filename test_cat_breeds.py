import pytest
from cat_breeds import api_app


@pytest.fixture(scope='module')
def http_client():
    testing_client = api_app.test_client()

    # Establish an application context before running the tests.
    ctx = api_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


def test_index_returns_200(http_client):
    response = http_client.get('/')
    assert response.status_code == 200
