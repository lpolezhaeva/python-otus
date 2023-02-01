from lab2_oop_and_pytest.src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        super().__init__(side_a, side_a)
        self.name = "Square"


