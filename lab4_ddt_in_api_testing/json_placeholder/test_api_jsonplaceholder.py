import pytest
import requests


def test_api_listing_all_resources(jsonplaceholder_api_base_url):
    """Listing all resources"""
    res = requests.get(jsonplaceholder_api_base_url)

    assert res.status_code == 200
    assert len(res.json()) == 100


def test_api_creating_source(jsonplaceholder_api_base_url):
    """Creating a resource"""
    myobj = {
        "title": "Title",
        "body": "Body",
        "userId": 123
    }
    res = requests.post(jsonplaceholder_api_base_url, json=myobj, headers={"Content-type": "application/json; charset=UTF-8"})

    assert res.status_code == 201

    assert res.json()["title"] == myobj["title"]
    assert res.json()["body"] == myobj["body"]
    assert res.json()["userId"] == myobj["userId"]
    assert res.json()["id"] == 101


@pytest.mark.parametrize("id_", [1, 2, 3, 4])
@pytest.mark.parametrize("user_id", [10, 20, 30, 40])
def test_api_updating_source(id_, user_id, jsonplaceholder_api_base_url):
    """Updating a resource"""
    myobj = {
        "id": id_,
        "title": "Updated_title",
        "body": "Updated_body",
        "userId": user_id
    }
    res = requests.put(jsonplaceholder_api_base_url + f"/{id_}", json=myobj, headers={"Content-type": "application/json; charset=UTF-8"})

    assert res.status_code == 200

    assert res.json()["title"] == myobj["title"]
    assert res.json()["body"] == myobj["body"]
    assert res.json()["userId"] == user_id
    assert res.json()["id"] == id_


@pytest.mark.parametrize("id_", [1, 2, 3, 4])
def test_api_patching_source(id_, jsonplaceholder_api_base_url):
    """Patching a resource"""
    myobj = {
        "title": "foo"
    }
    res = requests.patch(jsonplaceholder_api_base_url + f"/{id_}", json=myobj, headers={"Content-type": "application/json; charset=UTF-8"})

    assert res.status_code == 200
    assert res.json()["title"] == myobj["title"]


def test_api_deleting_source(jsonplaceholder_api_base_url):
    """Deleting a resource"""
    res = requests.delete(jsonplaceholder_api_base_url + "/1")

    assert res.status_code == 200
