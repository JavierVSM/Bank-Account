class BankAccount:
    all_accounts = []
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        print ("Your deposit was succeed. You have $", self.balance, "in your account")
        return self
      
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print ("Your withdrawal was succeed. You have $", self.balance, "in your account")
            return self
        else:
            print( "Insufficient funds: Charging a $5 fee." )
            self.balance -= 5
            return self
        
        
    def display_account_info(self):
         print ("Your balance: $", self.balance)
         return self
  

        
    def yield_interest(self):
        if self.balance >= 0:
            self.interest = self.balance * self.int_rate
            self.balance = self.balance + self.interest
            return self

    @classmethod
    def accountsInfo (cls):
        for account in cls.all_accounts:
            print( "Account balance:", account.balance, "Interest Rate:", account.int_rate)

A001 = BankAccount(0.05,0)
A002 = BankAccount(0.05,0)
A003 = BankAccount(0.05,0)

print ("=== Deposit Test ===")
A001.deposit (100)
A002.deposit (1000)
print (" ")
print ("=== Withdraw Test ===")
A001.withdraw (50)
A002.withdraw (500)
A003.withdraw (1000)
print (" ")
print ("===  Yield Interest Test ===")
A001.yield_interest ()
A002.yield_interest ()
A003.yield_interest ()
print (" ")
print ("===  Display Info Test ===")
A001.display_account_info ()
A002.display_account_info ()
A003.display_account_info ()
print (" ")
print ("- To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)")
print (" ")

A001.deposit(100).deposit(200).deposit(200).withdraw(300).yield_interest().display_account_info()

print (" ")
print ("- To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)")
print (" ")

A002.deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

print (" ")
print ("- NINJA BONUS: use a classmethod to print all instances of a Bank Account's info")
print (" ")

BankAccount.accountsInfo()
