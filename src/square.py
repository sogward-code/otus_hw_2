from otus_hw_2.src.figure import Figure


class Square(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Стороны должны быть положительными")
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return self.side * 4
