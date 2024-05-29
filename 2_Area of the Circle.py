class Circle:
    def __init__(self, radius):  # Constructor with single parameter radius
        self.radius = radius  # Instance variable self.radius is initialized with the provided radius value

    def area(self):  # Method to return the area
        return 3.141 * self.radius ** 2


circle = Circle(50)  # Create an instance of Circle class with radius
print(f"Area of {circle.radius} is {circle.area():.2f}")  # Print the output
