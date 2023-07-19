class Vehicles:
    def __init__(self,name, color, worth):
        self.name = name
        self.color = color
        self.worth = worth
    def description(self):
        print("this car is call %s worth:%.2f color is %s"
              % (self.name, self.worth, self.color))

car1 = Vehicles("Fer", "red", 9000.00)
car2 = Vehicles("Jump", "blue", 9000.00)
car1.description()
car2.description()