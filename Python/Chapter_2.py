# OOP - Object-Oriented Programming
class City:
    def __init__(self, name, population):  # acts as a constructor
        self.name = name  # self keyword refers to current instance
        self.population = population

    def describecity(self):
        print("In describeCity method...")
        print(f"The name of the city is {self.name}")
        print(f"The population of the city is {self.population}")


class State:
    def __init__(self, name):
        self.name = name

    def describestate(self):
        print(f"The name of the state is {self.name}")


# Object creation is not required for this file since we use this file in another file
# mumbai = City("Mumbai", 1000000)
# maharashtra = State("Maharashtra")
# mumbai.describecity()
# maharashtra.describestate()

