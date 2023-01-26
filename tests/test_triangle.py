import pytest
from src.triangle import Triangle


def test_triangle_init_positive():
    triangle = Triangle(3, 4, 5)
    assert triangle.name == "Triangle", "Triangle name is incorrect"
    assert triangle.side_a == 3, "side_a is incorrect"
    assert triangle.side_b == 4, "side_b is incorrect"
    assert triangle.side_c == 5, "side_c is incorrect"


def test_triangle_init_negative():
    with pytest.raises(ValueError, match="Triangle does not exist"):
        Triangle(5, 20, 30) 


def test_triangle_area_positive():
    triangle = Triangle(3, 4, 5)
    assert triangle.area == 6.0


def test_triangle_perimeter_positive():
    triangle = Triangle(3, 4, 5)
    assert triangle.perimeter == 12


