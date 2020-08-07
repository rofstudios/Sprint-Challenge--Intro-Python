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

# BASS 
class Vehicle:
    pass

# G from V
class GroundVehicle(Vehicle):
    pass

# C from G
class Car(GroundVehicle):
    pass

# M from G
class Motorcycle(GroundVehicle):
    pass

# F from V
class FlightVehicle(Vehicle):
    pass

# A from F
class Airplane(FlightVehicle):
    pass

# S from V
class Starship(FlightVehicle):
    pass