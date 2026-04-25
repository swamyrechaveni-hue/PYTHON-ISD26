# Base class representing a general vehicle with common attributes
class Vehicle:
    def __init__(self, colour, weight, max_speed, max_range=None, seats=None):
        # Core attributes shared across all vehicle types
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.max_range = max_range
        self.seats = seats

    def move(self, speed):
        """
        Generic movement method to be overridden by subclasses
        for more specific behavior.
        """
        print(f"The vehicle is moving at {speed} km/h")


# Car inherits from Vehicle and introduces form factor
class Car(Vehicle):
    def __init__(self, colour, weight, max_speed, form_factor, **kwargs):
        # Pass shared attributes to parent constructor
        super().__init__(colour, weight, max_speed, **kwargs)
        self.form_factor = form_factor

    def move(self, speed):
        # Overrides base method to reflect car-specific movement
        print(f"The car is driving at {speed} km/h")


# Electric car specialization with battery-specific attribute
class Electric(Car):
    def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.battery_capacity = battery_capacity

    def move(self, speed):
        # Includes additional context such as range
        print(f"The electric car is driving at {speed} km/h and has range {self.max_range}")


# Petrol car specialization with fuel capacity attribute
class Petrol(Car):
    def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.fuel_capacity = fuel_capacity

    def move(self, speed):
        print(f"The petrol car is driving at {speed} km/h and has range {self.max_range}")


# Plane inherits from Vehicle and adds aviation-specific property
class Plane(Vehicle):
    def __init__(self, colour, weight, max_speed, wingspan, **kwargs):
        super().__init__(colour, weight, max_speed, **kwargs)
        self.wingspan = wingspan

    def move(self, speed):
        # Overrides movement to represent flying
        print(f"The plane is flying at {speed} km/h")


# Propeller plane specialization
class Propeller(Plane):
    def __init__(self, colour, weight, max_speed, wingspan, propeller_diameter, **kwargs):
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.propeller_diameter = propeller_diameter

    def move(self, speed):
        print(f"The propeller plane is flying at {speed} km/h")


# Jet plane specialization with engine thrust attribute
class Jet(Plane):
    def __init__(self, colour, weight, max_speed, wingspan, engine_thrust, **kwargs):
        super().__init__(colour, weight, max_speed, wingspan, **kwargs)
        self.engine_thrust = engine_thrust

    def move(self, speed):
        print(f"The jet is flying at {speed} km/h")


# Multiple inheritance combining Car and Plane capabilities
class FlyingCar(Car, Plane):
    def __init__(self, colour, weight, max_speed, form_factor, wingspan, **kwargs):
        # Uses cooperative multiple inheritance via super()
        super().__init__(colour, weight, max_speed, form_factor=form_factor, wingspan=wingspan, **kwargs)

    def move(self, speed):
        # Unified behavior representing both driving and flying
        print(f"The flying car is driving or flying at {speed} km/h")


# Test objects demonstrating polymorphism across the class hierarchy
electric = Electric("green", 1200, 200, "Hatchback", 100, max_range=400, seats=5)
petrol = Petrol("red", 1500, 250, "SUV", 50, max_range=500)

plane = Plane("white", 5000, 800, 30)
jet = Jet("black", 6000, 900, 35, 20000)

flying = FlyingCar("blue", 1000, 200, "SUV", 20, seats=4)

# Iterates through different object types and calls their respective move methods
for obj in [electric, petrol, plane, jet, flying]:
    obj.move(100)