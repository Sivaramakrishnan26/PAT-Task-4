# Base class
class TV:
    def __init__(self, brand):  # Constructor
        self.brand = brand
        self.channel = 1
        self.volume = 50

    def increase_volume(self):  # Method to increase volume
        self.volume = min(self.volume + 1, 100)  # Increase the volume by +1 till 100

    def decrease_volume(self):  # Method to decrease volume
        self.volume = max(self.volume - 1, 0)  # Decrease the volume by -1 till 0

    def set_channel(self, channel):  # Method to set channel
        if 1 <= channel <= 50:  # TV has channel from 1 to 50
            self.channel = channel

    def reset_tv(self):  # Method to reset the TV to default settings
        self.channel = 1
        self.volume = 50

    def status(self):  # Method to return the TV status
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


x = input("Enter a Brand Name: ")  # Get a Brand Name from the user
tv = TV(x)  # Create an instance of the TV class with the specific brand
print(tv.status())  # Print the status
tv.increase_volume()
print(tv.status())  # Print the status after increasing volume
tv.decrease_volume()
print(tv.status())  # Print the status after decreasing volume
y = int(input("Enter Channel Number: "))  # Get a Channel Number from the user
tv.set_channel(y)  # Set the Channel
print(tv.status())  # Print the status after setting the channel


# Derived class 1
class LedTV(TV):  # LedTV class inherits the TV class
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_info(self):  # Method to display the details of LedTV
        return (
            f"LedTV     - Brand: {self.brand}, Thickness: {self.screen_thickness}mm, Energy Usage: {self.energy_usage}, "
            f"Lifespan: {self.lifespan}years, Refresh Rate: {self.refresh_rate}Hz")


print("\n")

# Get the details from the user
a = int(input("Enter Screen Thickness (mm): "))
b = str(input("Enter Energy Usage (High, Medium, Low): "))
c = int(input("Enter Lifespan (years): "))
d = int(input("Enter Refresh Rate (Hz): "))
ledtv = LedTV(x, a, b, c, d)  # Create an instance of the LedTV class with the given details
print(ledtv.display_info())  # Print the details of LedTV


# Derived class 2
class PlasmaTV(TV):  # PlasmaTV class inherits the TV class
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_info(self):  # Method to display the details of PlasmaTV
        return (
            f"PlasmaTV  - Brand: {self.brand}, Thickness: {self.screen_thickness}mm, Energy Usage: {self.energy_usage}, "
            f"Lifespan: {self.lifespan}years, Refresh Rate: {self.refresh_rate}Hz")


# e = int(input("Enter Screen Thickness (mm): "))
# f = str(input("Enter Energy Usage (High, Medium, Low): "))
# g = int(input("Enter Lifespan (years): "))
# h = int(input("Enter Refresh Rate (Hz): "))
plasmatv = PlasmaTV(x, a, b, c, d)  # Create an instance of the PlasmaTV class with the given details
print(plasmatv.display_info())  # Print the details of PlasmaTV
