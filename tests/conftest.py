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


# def pytest_generate_tests(metafunc):
#     # This is called for every test. Only get/set command line arguments
#     # if the argument is specified in the list of test "fixturenames".
#     option_value = metafunc.config.option.name
#     if "project_id" in metafunc.fixturenames and option_value is not None:
#         metafunc.parametrize("project_id", [option_value])
