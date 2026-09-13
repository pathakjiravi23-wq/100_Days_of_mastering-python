class Vehicle:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def vehicle_color(self):
        print("Vehicle's color:", self.color)


class Car(Vehicle):
    def __init__(self, name, model, color):
        super().__init__(name, model, color)

    def details(self):
        print("Name of the Vehicle:", self.name)
        super().vehicle_color()
        print("Models:", self.model)


class ElectricCar(Car):
    def __init__(self, name, model, color, fuelType):
        self.fuel = fuelType
        super().__init__(name, model, color)

    def car_details(self):
        print("Fuel Type:", self.fuel)
        super().details()


s1 = Vehicle("Truck", "Gen2", "Brown")
s1.vehicle_color()

s2 = Car("Mercedes", "V10", "Navy Blue")
s2.details()

s3 = ElectricCar("Mahindra", "Aurora", "RED", "Electric")
s3.car_details()
