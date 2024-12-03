class VowelCounter:  # class creation
    def __init__(self, str):
        self.str = str  # public attribute
    
    def count_vowels(self):  # method to count vowels in the string
        count = 0
        for s in self.str:
            if s.lower() in 'aeiou':  # for 'aeiou'
                count += 1
            elif s.upper() in 'AEIOU':  # for 'AEIOU'
                count += 1
        return count


str = input("Enter the string: ")  # takes user input
vc = VowelCounter(str)  # object creation
print(vc.count_vowels())  # function call
