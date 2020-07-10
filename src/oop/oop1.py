# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle --> **BASE CLASS**
class Vehicle:
    pass

# GroundVehicle --> Child of Vehicle
class GroundVehicle(Vehicle):
    pass

# FlightVehicle --> Child of Vehicle
class FlightVehicle(Vehicle):
    pass

# Car --> Child of GroundVehicle
class Car(GroundVehicle):
    pass

# Motorcyle --> Child of GroundVehicle
class Motorcycle(GroundVehicle):
    pass

# Airplane --> Child of FlightVehicle
class Airplane(FlightVehicle):
    pass

# Starship --> Child of FlightVehicle
class Starship(FlightVehicle):
    pass