from otus_hw_2.src.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, a, b, c):
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Невозможно создать треугольник")
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c
