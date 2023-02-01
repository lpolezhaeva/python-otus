import pytest
from lab2_oop_and_pytest.src.rectangle import Rectangle
from lab2_oop_and_pytest.src.triangle import Triangle


def test_add_area_positive():
    rectangle = Rectangle(2, 3)
    triangle = Triangle(3, 4, 5)
    assert rectangle.add_area(triangle) == 12.0


def test_add_area_negative():
    string = "ABC"
    triangle = Triangle(3, 4, 5)
    with pytest.raises(ValueError, match="Parameter 'figure' should be a subclass of Figure"):
        triangle.add_area(string)
