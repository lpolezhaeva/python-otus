import pytest
import requests
from jsonschema import validate


# Listing all resources
def test_api_listing_all_resources(base_url):
    res = requests.get(base_url)

    assert len(res.json()) == 100


# Creating a resource
def test_api_creating_source(base_url):
    myobj = {
        "title": "Title",
        "body": "Body",
        "userId": 123
    }
    res = requests.post(base_url, json=myobj, headers={"Content-type": "application/json; charset=UTF-8"})

    assert res.status_code == 201

    assert res.json()["title"] == myobj["title"]
    assert res.json()["body"] == myobj["body"]
    assert res.json()["userId"] == myobj["userId"]
    assert res.json()["id"] == 101


# Updating a resource
@pytest.mark.parametrize("id_", [1, 2, 3, 4])
@pytest.mark.parametrize("user_id", [10, 20, 30, 40])
def test_api_updating_source(id_, user_id, base_url):
    myobj = {
        "id": id_,
        "title": "Updated_title",
        "body": "Updated_body",
        "userId": user_id
    }
    res = requests.put(base_url + f"/{id_}", json=myobj, headers={"Content-type": "application/json; charset=UTF-8"})

    assert res.status_code == 200

    assert res.json()["title"] == myobj["title"]
    assert res.json()["body"] == myobj["body"]
    assert res.json()["userId"] == user_id
    assert res.json()["id"] == id_


# Patching a resource
@pytest.mark.parametrize("id_", [1, 2, 3, 4])
def test_api_patching_source(id_, base_url):
    myobj = {
        "title": "foo"
    }
    res = requests.patch(base_url + f"/{id_}", json=myobj, headers={"Content-type": "application/json; charset=UTF-8"})

    assert res.status_code == 200
    assert res.json()["title"] == myobj["title"]


# Deleting a resource
def test_api_deleting_source(base_url):
    res = requests.delete(base_url + "/1")

    assert res.status_code == 200
