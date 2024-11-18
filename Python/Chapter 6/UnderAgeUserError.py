# Custom Exceptions
# Flow is define-raise-handle
class UnderAgeUserError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


age = int(input("Enter your age: "))
try:
    if age < 18:
        raise UnderAgeUserError("You are underage to be a voter")   # we raise the user-defined exception
except UnderAgeUserError as uag:  # uag becomes the object
    print(uag.message)   # we get the above message
else:
    print("Age appropriate")
