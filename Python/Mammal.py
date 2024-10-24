# Inheritance in Python for Chapter_2.py
class Mammal:
    __sound = None  # private variable

    def __init__(self, name, lifespan, habitat, sound):
        self.name = name
        self.lifespan = lifespan
        self.habitat = habitat
        self.__sound = sound
        print("Mammal object created...")
    
    def describe(self):
        print(f"The name of the mammal is {self.name}")
        print(f"The lifespan of the mammal is {self.lifespan}")
        print(f"The habitat of the mammal is {self.habitat}")
        print(f"The sound of the mammal is {self.__sound}")


class Bat(Mammal):  # inherits the mammal class
    def __init__(self, name, lifespan, habitat, sound, diet):
        super().__init__(name, lifespan, habitat, sound)  # inherits the variables from parent class
        self.diet = diet
        print("Bat object created...")

    def describe(self):  # method overriding
        super().describe()  # inherits the describe method from parent class
        print(f"The diet of the bat is {self.diet}")


b = Bat("Whale", 70, "Aquatic", "Carnivorous", "Harsh")
b.describe()
print(b.__sound)  # private variable cannot be inherited
