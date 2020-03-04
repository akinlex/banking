class Account:
    # Constants. For one reason or the other, I didn't use the atm_charge variable lol... 
    transfer_charge, withdraw_charge, atm_charge = 10.75, 65.00, 1000

    def __init__(self, acct_no, name, surname, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
        self.surname = surname

    # Deposit money
    def deposit(self, amount):
        try:
            self.balance +=  amount
            return f'Deposited {amount}'
        except:
            print("An error occurred!!!")

    # Withdraw money
    def withdraw(self, amount):
        try:
            if self.balance - amount >= self.min_balance:
                amount += Account.withdraw_charge
                self.balance -= amount
                return f'Withdrew {amount}' 
            else:
                print(f"{self.name}, Sorry, you do not enough funds!")
        except:
            print("An error occurred!!!")

    # Transfer money
    def transfer(self, amount):
        try:
            if self.balance - amount >= self.min_balance:
                amount += Account.transfer_charge
                self.balance -= amount 
                return f'Transferred {amount}'
            else:
                print(f"{self.name}, Sorry, you do not enough funds!")
        except:
            print("An error occurred!!!")
    
    # Check account balance
    def check_balance(self):
        try:
            print(f"{self.name}'s Account Balance: {self.balance}")
        except:
            print("An error occurred!!!")

class Current_Account(Account): #Inheritance
    def __init__(self, acct_no, name, surname, balance):
        super().__init__(acct_no, name, surname, balance,  min_balance = -2000 )

    def __str__(self):
        return f"{self.name}'s Current Account Balance: {self.balance}"

class Savings_Account(Account): #Inheritance
    def __init__(self, acct_no, name, surname, balance):
        super().__init__(acct_no, name, surname, balance,  min_balance = 0)

    def deposit(self, amount): # Polymorphism
        if amount < 1000000:
            self.balance +=  amount
        else:
            print(f"{self.name}, You cannot make a deposit of above N1,000,000, please contact your bank!!!")

    def __str__(self):
        return f"{self.name} Savings Account Balance: {self.balance}"

class Salary_Account(Account): #Inheritance
    def __init__(self, acct_no, name, surname, balance):
        super().__init__(acct_no, name, surname, balance,  min_balance = 0)

    def request_loan(self, amount):
        if self.balance > amount:
            print("You are not eligible for a loan")
        else:
            self.balance += amount

    def __str__(self):
        return f"{self.name}'s Salary Account Balance: {self.balance}"

class Young_Account(Account): # Inheritance
    def __init__(self, acct_no, name, surname, balance, age):
        if age < 18:
            super().__init__(acct_no, name, surname, balance, min_balance = 0)
        else:
            print("You are an Adult, Please open another account")

    def deposit(self, amount):
        try:
            if amount < 20000:
                self.balance +=  amount
            else:
                print(f"{self.name}, You cannot make a deposit of above N50,000, please contact your bank!!!")
        except:
            print("An error occurred!!!")
    def __str__(self):
        return f"{self.name} Savings Account Balance: {self.balance}"

# Instantiation
Account1 = Savings_Account(100001, "Wale", "Aderibigbe", 20000)

print("\n")
print('Depositing...')
Account1.deposit(3000000)
Account1.check_balance()
print('Withdrawing...')
Account1.withdraw(12000)
print('Withdrawn')
print('Checking balance...')
Account1.check_balance()

Account2 = Salary_Account(100002, "Tobi", "Alakija", 3000)

print("\n")
print('Depositing...')
Account2.deposit(1000)
print('Deposited')
print('Checking balance...')
Account2.check_balance()
Account2.transfer(1000)
print('Checking balance...')
Account2.check_balance()
print('Requesting...')
Account2.request_loan(20000)
print('Requested')
print('Checking balance...')
Account2.check_balance()

Account3 = Young_Account(100003, "Akin", "Peters", 3000, 17)

print("\n")
print('Depositing...')
Account3.deposit(20000)
print('Deposited')
print('Checking balance...')
Account3.check_balance()
print('Transferring...')
Account3.transfer(1000)
print('Transferred')
print('Checking balance...')
Account3.check_balance()

Account4 = Current_Account(100004, "Moses", "Ogundele", 1000000)

print("\n")
print('Depositing...')
Account4.deposit(25000)
print('Deposited')
print('Checking balance...')
Account4.check_balance()
print('Transferring...')
Account4.transfer(5000)
print('Transferred')
print('Checking balance...')
Account4.check_balance()