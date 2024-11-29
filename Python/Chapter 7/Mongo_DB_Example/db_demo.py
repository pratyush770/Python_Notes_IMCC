# Any method which starts with __ and ends with __ is called as a 'dunder' method
class Student:
    @staticmethod   # if we make a method static, it does not require self keyword and does not create an object
    def values(name, age, isIntelligent):
        return {
            "name": name,
            "age": age,
            "isIntelligent": isIntelligent
        }
        