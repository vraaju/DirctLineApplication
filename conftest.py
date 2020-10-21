import pytest

from app import app as additions_app


@pytest.fixture
def app():
    yield additions_app


@pytest.fixture
def client(app):
    return app.test_client() 