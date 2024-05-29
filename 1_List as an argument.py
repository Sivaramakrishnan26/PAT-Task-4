class Circle:
    def __init__(self, list1):  # Constructor with single parameter list1
        self.list1 = list1  # Instance variable self.list1 is initialized with the provided list1 value

    def read_list(self):  # Method to read the list
        print(f"List: {self.list1}")  # Print the list


circle = Circle([10, 501, 22, 37, 100, 999, 87, 351])  # Create an instance of Circle class with list1

circle.read_list()  # Invoke the read_list() method on the circle instance

print("\n--------------------------------------------------\n")


class Circle:
    def __init__(self, radius_list):  # Constructor with single parameter radius_list
        self.radius_list = radius_list  # Instance variable self.radius_list is initialized with the provided radius_list value

    def area(self):  # Method to calculate area from the radius_list
        area1 = []
        for radius in self.radius_list:
            area = 3.141 * radius ** 2
            area1.append(area)
        return area1


radius = [10, 501, 22, 37, 100, 999, 87, 351]  # List of radius
circle = Circle(radius)  # Create an instance of Circle with radius_list
area_list = circle.area()  # Invoke the area() method on the circle instance
print([round(x, 2) for x in area_list])  # Print the list of area with the decimal point round to 2

# Print the area for each radius separately
for i, radius1 in enumerate(radius):
    print(f"Area of the circle with radius {radius1} is {area_list[i]:.2f}")
