import pytest
import requests
import re
import json
from jsonschema import validate


# LIST ALL BREEDS response schema validation
def test_api_json_schema(base_url):
    res = requests.get(base_url + "/breeds/list/all")

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

    validate(instance=res.json(), schema=schema)


# BREEDS LIST
@pytest.mark.parametrize("breed", ["Affenpinscher", "Akita", "Maltese", "Scottish Deerhound", "Pug"])
def test_api_breeds_list(breed, base_url):
    breed_response = breed
    breed_answer = breed

    if " " in breed:
        breed_part_list = breed.split()
        breed_response = breed_part_list[1] + "/" + breed_part_list[0]
        breed_answer = breed_part_list[1] + "-" + breed_part_list[0]
    res = requests.get(base_url + f"/breed/{breed_response.lower()}/images/random")

    assert res.status_code == 200
    assert re.findall(f"https://images.dog.ceo/breeds/{breed_answer.lower()}/*", res.content.decode())


# LIST ALL SUB-BREEDS
@pytest.mark.parametrize("breed", ["Terrier", "Akita", "Maltese", "Setter", "Pug"])
def test_api_sub_breed(breed, base_url):
    breed_lower_case = breed.lower()

    response_breeds = requests.get(base_url + "/breeds/list/all")
    response_dict = json.loads(response_breeds.text)
    breeds = response_dict["message"]

    response_sub_breeds = requests.get(base_url + f"/breed/{breed_lower_case}/list")
    response_dict_1 = json.loads(response_sub_breeds.text)
    sub_breeds = response_dict_1["message"]

    assert response_breeds.status_code == 200
    assert breeds[breed_lower_case] == sub_breeds[breed_lower_case]


# BY BREED
def test_api_image_by_breed(base_url, breed="Akita"):
    res_all = requests.get(base_url + f"/breed/{breed.lower()}/images").json()["message"]
    res_random = requests.get(base_url + f"/breed/{breed.lower()}/images/random").json()["message"]

    assert res_random in res_all


# MULTIPLE IMAGES FROM A BREED COLLECTION
@pytest.mark.parametrize("image_num", [3, 1])
@pytest.mark.parametrize("breed", ["Hound", "Akita", "Maltese", "Setter", "Pug"])
def test_api_multiple_images_from_breed_collection(image_num, breed, base_url):
    res = requests.get(base_url + f"/breed/{breed.lower()}/images/random/{image_num}")

    assert res.status_code == 200
    assert len(res.json()["message"]) == image_num
