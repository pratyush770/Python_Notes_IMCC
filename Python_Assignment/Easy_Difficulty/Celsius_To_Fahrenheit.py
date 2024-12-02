class Celsius_To_Fahrenheit:
    def __init__(self, celsius):
        self.celsius = celsius
    def celsiusToFahrenheit(self):  # function to convert celsius to fahrenheit
        f = (9 / 5) * self.celsius + 32  # formula to convert celsius to fahrenheit
        print(f"The temperature in celsius {self.celsius} after converting is {f} fahrenheit")
