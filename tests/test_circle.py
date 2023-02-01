import pytest
import math
from src.circle import Circle


def test_circle_init_positive():
    circle = Circle(6)
    assert circle.name == "Circle", "Circle name is incorrect"
    assert circle.radius == 6, "radius is incorrect"


def test_circle_init_negative():
    with pytest.raises(ValueError, match="Circle does not exist"):
        Circle(-1)


def test_circle_area_positive():
    circle = Circle(10)
    assert circle.area == math.pi * 10 ** 2


def test_circle_perimeter_positive():
    circle = Circle(5)
    assert circle.perimeter == 2 * math.pi * 5
