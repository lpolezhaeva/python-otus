from lab2_oop_and_pytest.src.rectangle import Rectangle


def test_rectangle_init_positive():
    rectangle = Rectangle(2, 3)
    assert rectangle.name == "Rectangle", "Rectangle name is incorrect"
    assert rectangle.side_a == 2, "side_a is incorrect"
    assert rectangle.side_b == 3, "side_b is incorrect"


def test_rectangle_area_positive():
    rectangle = Rectangle(3, 4)
    assert rectangle.area == 12.0


def test_rectangle_perimeter_positive():
    rectangle = Rectangle(3, 4)
    assert rectangle.perimeter == 14.0
