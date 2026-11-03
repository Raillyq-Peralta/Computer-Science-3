# Raillyq Lairdswill S. Peralta | Rachel Bocalan
# 9 - Lithium | 11-03-26

'''
GUIDE QUESTIONS
a. What is duck typing, as explained in the video?
    > Duck typing is a programming concept in which the type or class of an object is defined by its own attributes and methods rather than its inheritance from a parent class.

b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
    > The Car class needed to have the same methods as the Dog and Cat classes, so it could be used in the same loop without causing an error.
'''

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()
vehicles = [car, boat, drone]

for vehicle in vehicles:
    start_trip(vehicle)

'''
This code demonstrates polymorphism because the start_trip function can accept any object that has a move method, regardless of its class.
The Car, Boat, and Drone classes all have a move method, allowing them to be used in the same function without any issues.
'''