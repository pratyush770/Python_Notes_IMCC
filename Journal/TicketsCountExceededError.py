class TicketsCountExceededError(Exception):  # user defined exception
    def __init__(self, msg):
        super().__init__(msg)  # calls the msg from Exception class
        self.msg = msg


tcount = int(input("Enter the number of tickets you want to buy: "))  # takes user input
try:
    if tcount > 5:
        raise TicketsCountExceededError("You cannot buy more than 5 tickets..")  # call user defined exception
except TicketsCountExceededError as tc_error:  # tc_error is the alias name
    print(tc_error.msg)  # print the msg
else:
    print("Tickets booked successfully!!")




