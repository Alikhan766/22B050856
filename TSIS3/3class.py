class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle:", 2 * (self.length + self.width))


l = 8
w = 12

a = Rectangle(l, w)
a.area()
