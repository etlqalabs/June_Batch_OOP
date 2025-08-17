class Car:
    def __init__(self,car_brand):
        self.car_brand = car_brand
        print("My car brand is ",self.car_brand)

    def print_car_name(self):
        print("hey this is Toyoto car")

c = Car("Maruti Suzuki")
c.print_car_name()