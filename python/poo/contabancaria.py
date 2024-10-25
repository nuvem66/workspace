class Account:
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
   
    def __str__(self) -> str:
        return f"\nAccount information: \nOwner: {self.name}. \nBalance: ${self.balance}."

    def withdraw(self, value):
        if value <= self.balance:
            self.balance = self.balance - value
            print(f"\nRealized with sucess! ${self.balance:.2f} is your new balance.")
        else:
            print(f"\nDenied. Your balance is not sufficient.")
    
    def add(self, value):
        self.balance = self.balance + value
        print(f"\nRealized with sucess. ${self.balance:.2f} is your new balance.")

#the thing that runs it:
if input("Wanna create an Account? y/N ") == "y":
    choosenname = input("Name: ")
    choosenbalance = int(input("Balance: "))
    acc1 = Account(choosenname, choosenbalance)
    print(f"_______________________________________________\n{acc1}")
   
    keepgoing = "y"

    while keepgoing == "y":
        action = int(input("\nWhat do you wanna do?\n[1] Make a deposit.\n[2] Make a withdrawal.\n[3] Exit\nYour action: "))
        if action  == 1:
            actionvalue = int(input("Value for your action: "))
            acc1.add(actionvalue)

            keepgoing = input("Wanna continue? y/N ")

        elif action == 2:
            actionvalue = int(input("Value for your action: "))
            acc1.withdraw(actionvalue)

            keepgoing = input("Wanna continue? y/N ")

        else:
            keepgoing = ""
    print(f"\n{acc1}")
    print("\nDone.")
else:
    print("Done.")