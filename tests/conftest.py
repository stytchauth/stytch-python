import pytest


def pytest_addoption(parser):
    parser.addoption("--project_id", action="store", default="default project_id")
    parser.addoption("--secret", action="store", default="default secret")
    parser.addoption("--email", action="store", default="default email")


@pytest.fixture(scope="session")
def project_id(request):
    return request.config.getoption("--project_id")


@pytest.fixture(scope="session")
def secret(request):
    return request.config.getoption("--secret")


@pytest.fixture(scope="session")
def email(request):
    return request.config.getoption("--email")
