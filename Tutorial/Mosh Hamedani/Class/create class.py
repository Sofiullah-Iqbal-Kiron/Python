# Pascal naming convention to name classes. First letter of every word should be uppercase.

class Point:
    # Class level attributes/static variables. They called by class name and distributed to all class instances.
    default_position = 0, 0  # Defined as a tuple.

    # Constructor/magic method.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Every methods in our classes should have at least one parameter called self referencing this object.
    def draw(self):
        print(f'Drawn a point in ({self.x}, {self.y}).')


# Create an object of Point type like call a function.
p1 = Point(1, 2)
p1.draw()
print(isinstance(p1, Point))
print(isinstance(p1, int))  # int is also a class in python. So far, so good.
print(p1.default_position)
