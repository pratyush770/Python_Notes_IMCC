# OOP - Object-Oriented Programming
class City:
    def __init__(self, name, population):  # acts as a constructor
        self.name = name  # self keyword refers to current instance
        self.population = population


mumbai = City("Mumbai", 1000000)


