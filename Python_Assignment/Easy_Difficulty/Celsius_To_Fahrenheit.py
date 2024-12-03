class Celsius_To_Fahrenheit:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsiusToFahrenheit(self):  # function to convert celsius to fahrenheit
        f = (9 / 5) * self.celsius + 32  # formula to convert celsius to fahrenheit
        return f


celsius = int(input("Enter the temperature in celsius: "))  # takes user input
c = Celsius_To_Fahrenheit(celsius)  # object creation
print(c.celsiusToFahrenheit())  # function call
