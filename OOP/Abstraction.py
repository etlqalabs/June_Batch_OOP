from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # concentrate
    def honk(self):
        print("Vehicle honks")


class Car(Vehicle):
    def start(self):
        print("Car starts...")

class ElectricCar(Car):
    def stop(self):
        print("Electrci car stops..")

class CallingClass:
    '''
    veh = Vehicle()
    veh.start()

    car = Car()
    car.start()
    car.stop()
     '''

    ec = ElectricCar()
    ec.start()
    ec.honk()
    ec.stop()
