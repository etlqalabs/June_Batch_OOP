# 1.  Method overloading ( Not supported in Python )

class MathsAddition:
    def add(self, n1,n2,n3):
            print(n1+n2+n3)

    def add(self, n1, n2):
        print(n1 + n2)


# 2. Method overriding

class Vehicle:
    def start(self):
        print("Vehicle starts...")

    def stop(self):
        print("Vehicle stops...")

class Car(Vehicle):
    def start(self):
        print("Car starts...")

class Bike(Vehicle):
    def stop(self):
        print("Bike stops...")



class CallingClass:
    print("Vehicle -base class ( parent )")
    veh = Vehicle()
    veh.start()
    veh.stop()

    print("Car -sub class ( child class)  class ")
    car = Car()
    car.start()
    car.stop()

    print("Bike -sub class ( child class)  class ")
    bike = Bike()
    bike.start()
    bike.stop()



    #obj = MathsAddition()
    #obj.add(2,4)


