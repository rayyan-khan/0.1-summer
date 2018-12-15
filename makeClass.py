import sys


class Car():
    price = 0
    brand = ''
    model = ''
    color = ''
    odo = 0

    def __init__(self, price = 35000, brand = "Toyota", model = "camry", color = "red", odo = 0):
        self.price = price
        self.brand = brand
        self.model = model
        self.color = color

    def changePrice(self, price):
        self.price = price

    def changeColor(self, color):
        self.color = color

    def drive(self, distance):
        self.odo = self.odo + distance

    def avgSpeed(self, time, distance):
        print((distance/time), " mph.")

    def descrip(self):
        print("Price: ", self.price, " Brand: ", self.brand, " Model: ", self.model, " Color: ", self.color, " Mileage: ", self.odo)

car1 = Car()
car1.descrip()
car1.drive(1000)
print(car1.odo)
car1.avgSpeed(300, 1500)

