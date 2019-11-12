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


def test_list_of_cat_breeds_is_available(http_client):
    response = http_client.get('/api/cat_breed/')
    assert response.status_code == 200


def test_list_of_cat_breeds(http_client):
    response = http_client.get('/api/cat_breed/')
    assert len(response.json) == 3


def test_bengal_is_a_cat_breed_in_the_list(http_client):
    response = http_client.get('/api/cat_breed/')
    assert "Bengal" in response.json
