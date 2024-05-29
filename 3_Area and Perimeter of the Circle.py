class Circle:
    def __init__(self, radius):  # Constructor with single parameter radius
        self.radius = radius  # Instance variable self.radius is initialized with the provided radius value

    def area(self):  # Method to return the area
        return 3.141 * self.radius ** 2

    def perimeter(self):  # Method to return the perimeter
        return 2 * 3.141 * self.radius


circle = Circle(5)  # Create an instance of Circle class with radius
print(f"Area of {circle.radius} is {circle.area()}")  # Print the area of the Circle
print(f"Perimeter of {circle.radius} is {circle.perimeter()}")  # Print the perimeter of the Circle
