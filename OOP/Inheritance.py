# parent class
class Vehicle:
    def start(self):
        print("vehicle starts..")

    def stop(self):
        print("vehicle stops..")

# child 1
class Car(Vehicle):
    def honk(self):
        print("Car honks")

    def power_break(self):
        print("Power break applied")

# child 2
class Bike(Car):
    def beep(self):
        print("Bike beeps")


class CallingClass:
    # creating object of parent class
    print("Methods called from Vehicle class")
    vehicle = Vehicle()
    vehicle.start()
    vehicle.stop()

   # create object of Car class ( child 1)
    print("Methods called from Car class")
    car = Car()
    car.start()
    car.honk()
    car.stop()

    # create object of Bike class ( child 2)
    print("Methods called from Bike class")
    bike = Bike()
    bike.power_break()




