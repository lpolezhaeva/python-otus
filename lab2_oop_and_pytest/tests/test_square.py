from lab2_oop_and_pytest.src.square import Square


def test_square_init_positive():
    square = Square(2)
    assert square.name == "Square", "Square name is incorrect"
    assert square.side_a == 2, "side_a is incorrect"
    assert square.side_b == 2, "side_b is incorrect"


def test_square_area_positive():
    square = Square(10)
    assert square.area == 100.0


def test_square_perimeter_positive():
    square = Square(5)
    assert square.perimeter == 20.0
