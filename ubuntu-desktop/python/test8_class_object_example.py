class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def get_speed(self):
        return self.speed

# Create a Car object and test its methods
car = Car('Toyota', 'Corolla', 2021)
print("Car make:", car.make)
print("Car model:", car.model)
print("Car year:", car.year)

car.accelerate()
print("Current speed:", car.get_speed())

car.brake()
print("Current speed:", car.get_speed())
