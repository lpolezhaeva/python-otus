import requests


def test_api_ya_ru(url, status_code):
    res = requests.get(url)
    assert res.status_code == status_code
