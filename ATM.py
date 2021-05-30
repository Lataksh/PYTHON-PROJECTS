class atm(object):
    def __init__(self, atmNumber, pinNumber):
        self.atmNumber = atmNumber,
        self.pinNumber = pinNumber

    def withdraw(self, amount):
        print("You want to withdraw " + amount.__str__() + "rs. from your account")
        print("Withdrawing the amount...")
        print("Succesfully withdrawn the amount from the account")

    def submitAmount(self, amount):
        print("You want to deposit " + amount.__str__() + "rs. from your account")
        print("depositing the amount...")
        print("Succesfully deposited the amount in the account")



accNo = int(input("Please enter your account number"))
pinNo = int(input("Please enter the pin code registered with the account number"))

account = atm(accNo, pinNo)
method = int(input("If you want to withdraw amount then press 1, if you want to deposit the amount press 2"))
if(method == 1):
    amount = int(input("Please enter the amount you want to withdraw"))
    account.withdraw(amount)
    method = int(input("If you want to withdraw amount then press 1, if you want to deposit the amount press 2"))

if (method == 1):
    amount = int(input("Please enter the amount you want to deposit"))
    account.submitAmount(amount)
    method = int(input("If you want to withdraw amount then press 1, if you want to deposit the amount press 2"))

