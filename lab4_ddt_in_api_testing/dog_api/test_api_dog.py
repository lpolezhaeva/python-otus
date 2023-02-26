import pytest
import requests
import re
import json
from jsonschema import validate


def test_api_json_schema(dog_api_base_url):
    """LIST ALL BREEDS response schema validation"""
    res = requests.get(dog_api_base_url + "/breeds/list/all")

    schema = {
        "message": {
            "type": "object",
            "patternProperties": {
                "^.*$": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "additionalProperties": False
        },
        "status": {"type": "string"},
        "required": ["message", "status"]
    }

    assert res.status_code == 200
    validate(instance=res.json(), schema=schema)


@pytest.mark.parametrize("breed", ["Affenpinscher", "Akita", "Maltese", "Scottish Deerhound", "Pyrenees"])
def test_api_breeds_list(breed, dog_api_base_url):
    """BREEDS LIST"""
    breed_response = breed
    breed_answer = breed

    if " " in breed:
        breed_part_list = breed.split()
        breed_response = breed_part_list[1] + "/" + breed_part_list[0]
        breed_answer = breed_part_list[1] + "-" + breed_part_list[0]
    res = requests.get(dog_api_base_url + f"/breed/{breed_response.lower()}/images/random")
    data = res.json()

    assert res.status_code == 200
    assert re.findall(f".*/{breed_answer.lower()}/.*\\.jpg", data['message'])


@pytest.mark.parametrize("breed", ["Terrier", "Akita", "Maltese", "Setter", "Pug"])
def test_api_sub_breed(breed, dog_api_base_url):
    """LIST ALL SUB-BREEDS"""
    breed_lower_case = breed.lower()

    response_breeds = requests.get(dog_api_base_url + "/breeds/list/all")
    response_dict = json.loads(response_breeds.text)
    breeds = response_dict["message"]

    response_sub_breeds = requests.get(dog_api_base_url + f"/breed/{breed_lower_case}/list")
    response_dict_1 = json.loads(response_sub_breeds.text)
    sub_breeds = response_dict_1["message"]

    assert response_breeds.status_code == 200
    assert breeds[breed_lower_case] == sub_breeds


def test_api_image_by_breed(dog_api_base_url, breed="Akita"):
    """BY BREED"""
    res_all = requests.get(dog_api_base_url + f"/breed/{breed.lower()}/images")
    res_random = requests.get(dog_api_base_url + f"/breed/{breed.lower()}/images/random")

    data_all = res_all.json()["message"]
    data_random = res_random.json()["message"]

    assert res_all.status_code == 200
    assert res_random.status_code == 200
    assert data_random in data_all


@pytest.mark.parametrize("image_num", [3, 1])
@pytest.mark.parametrize("breed", ["Hound", "Akita", "Maltese", "Setter", "Pug"])
def test_api_multiple_images_from_breed_collection(image_num, breed, dog_api_base_url):
    """ULTIPLE IMAGES FROM A BREED COLLECTION"""
    res = requests.get(dog_api_base_url + f"/breed/{breed.lower()}/images/random/{image_num}")

    assert res.status_code == 200
    assert len(res.json()["message"]) == image_num
