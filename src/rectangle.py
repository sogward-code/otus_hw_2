from otus_hw_2.src.figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Стороны должны быть положительными и больше 0")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)
