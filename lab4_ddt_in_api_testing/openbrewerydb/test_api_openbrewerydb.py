import pytest
import requests
from jsonschema import validate


# Single Brewery response schema validation
def test_api_json_schema(base_url, obdb_id="madtree-brewing-cincinnati"):
    res = requests.get(base_url + f"/{obdb_id}")

    schema = {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "brewery_type": {"type": "string"},
        "street": {"type": "string"},
        "address_2": {
            "anyOf": [
                {"type": "string"},
                {"type": None}
            ]},
        "address_3": {"anyOf": [
            {"type": "string"},
            {"type": None}
        ]},
        "city": {"type": "string"},
        "state": {"type": "string"},
        "county_province": {"anyOf": [
            {"type": "string"},
            {"type": None}
        ]},
        "postal_code": {"type": "string"},
        "country": {"type": "string"},
        "longitude": {"type": "string"},
        "latitude": {"type": "string"},
        "phone": {"type": "string"},
        "website_url": {"type": "string"},
        "updated_at": {"type": "string"},
        "created_at": {"type": "string"},
        "minProperties": 17
    }

    validate(instance=res.json(), schema=schema)


# by_id
def test_api_by_id(base_url, brewery_id="madtree-brewing-cincinnati"):
    res = requests.get(base_url + f"/{brewery_id}")

    assert res.status_code == 200
    assert res.json()["id"] == brewery_id


# by_state
@pytest.mark.parametrize("brewery_state", ["new_york", "california", "indiana", "oregon"])
def test_api_by_type(brewery_state, base_url):
    res = requests.get(base_url + f"?by_state={brewery_state}")
    brewery_state_list = list(map(lambda x: x.get('brewery_state'), res.json()))

    assert res.status_code == 200
    assert brewery_state_list
    assert all(brewery_state == item for item in brewery_state_list)


# by_type
@pytest.mark.parametrize("brewery_type", ["micro", "nano", "regional", "brewpub", "large",
                                          "planning", "bar", "contract", "closed"])
def test_api_by_type(brewery_type, base_url):
    res = requests.get(base_url + f"?by_type={brewery_type}")
    brewery_type_list = list(map(lambda x: x.get('brewery_type'), res.json()))

    assert res.status_code == 200
    assert brewery_type_list
    assert all(brewery_type == item for item in brewery_type_list)


# per_page
@pytest.mark.parametrize("page_num", [1, 5, 3, 10])
def test_api_per_page(page_num, base_url):
    res = requests.get(base_url + f"?per_page={page_num}")

    assert res.status_code == 200
    assert len(res.json()) == page_num



