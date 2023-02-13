class Shape:
    pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print("Length of Square:", self.length)
        print("Area of Square:", self.length ** 2)


n = Square(5)
n.area()
