from script.deploy import deploy_favorites
import pytest


@pytest.fixture(scope="session") # This fixture will be executed only once per test session but is it is function then it will be executed every time it is called and when this is module then it will be executed only once per test session
def favorites():
    return deploy_favorites()