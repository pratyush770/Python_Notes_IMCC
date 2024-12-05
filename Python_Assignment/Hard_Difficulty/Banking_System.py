class bankingSystem:  # class creation
    def __init__(self, acn, type, bal):  # initialize a constructor with 3 parameters 
        self.acn = acn  # public attribute
        self.type = type
        self.bal = bal
        self._total_bal = 0  # private attribute

    def account_creation(self):  # function to print account details
        print("Account created successfully")
        print(self.acn)
        print(self.type)
        print(self.bal)

    def deposit(self):  # function to deposit amount
        dep = int(input("Enter the amount you want to deposit: "))
        print("Deposited amount: ", dep)
        self._total_bal = self.bal + dep

    def withdraw(self):  # function to withdraw amount
        wth = int(input("Enter the amount you want to withdraw: "))
        print("Withdraw amount: ", wth)
        self._total_bal = self._total_bal - wth

    def balance_inquiry(self):  # function to check total balance
        print("Total balance: ", self._total_bal)


acn = int(input("Enter the account number: "))  # takes user input
ac_type = input("Enter the type of account: ")
bal = int(input("Enter the initial balance: "))   
bs = bankingSystem(acn, ac_type, bal)  # object creation
bs.account_creation()  # function call
bs.deposit() 
bs.withdraw()
bs.balance_inquiry()