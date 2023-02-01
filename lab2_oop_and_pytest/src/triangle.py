import math

from lab2_oop_and_pytest.src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b < side_c or side_a + side_c < side_b or side_b + side_c < side_a:
            raise ValueError("Triangle does not exist")

        super().__init__("Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        half_perimeter = self.perimeter / 2.0
        return math.sqrt(half_perimeter * (half_perimeter - self.side_a) * (half_perimeter - self.side_b) *
                         (half_perimeter - self.side_c))


