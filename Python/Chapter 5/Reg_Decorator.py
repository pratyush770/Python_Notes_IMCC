import re
# pseudo decorator function

class Session:
    # self is not required for static method and no need to create an object
    @staticmethod  # annotation
    def random_number():
        return 5


print(Session.random_number())
# decorators are simple functions
# we need to know callback, closure, execution context and *args,**kwargs


def log(incoming_func):
    def caller(*args, **kwargs):
        print("Calling the function")
        result = incoming_func(*args, **kwargs)
        return result
    return caller

@log
def add(n1, n2):
    return n1 + n2

@log
def sub(n1, n2):
    return n1 - n2


print(add(5, 8))
print(sub(8, 5))

# Any function that uses anything outside its scope is known as impure functions

