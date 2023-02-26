import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://api.openbrewerydb.org/breweries",
                     help="Brewery API Url")


@pytest.fixture(scope="session")
def openbrewerydb_api_base_url(request):
    return request.config.getoption("--url")
