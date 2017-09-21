# encoding=utf8

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def calculate_area(self):
        return self.width * self.height


rect1 = Rectangle(2,3)
print 'size = ', rect1.calculate_area()
rect2 = Rectangle(3,5)
print 'size = ', rect2.calculate_area()