import pytest


def pytest_addoption(parser):
    parser.addoption("--project_id", action="store", default="default project_id")
    parser.addoption("--secret", action="store", default="default secret")


@pytest.fixture(scope="session")
def project_id(request):
    return request.config.getoption("--project_id")


@pytest.fixture(scope="session")
def secret(request):
    return request.config.getoption("--secret")
