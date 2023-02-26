import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://dog.ceo/api",
                     help="Dog API Url")


@pytest.fixture(scope="session")
def dog_api_base_url(request):
    return request.config.getoption("--url")

