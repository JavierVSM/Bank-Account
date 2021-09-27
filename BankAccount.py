class BankAccount:
    
    def __init__(self):
        self.int_rate = 0.05
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print ("Your deposit was succeed. You have $", self.balance, "in your account")
      
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print ("Your withdrawal was succeed. You have $", self.balance, "in your account")
        else:
            print( "Insufficient funds: Charging a $5 fee." )
            self.balance -= 5
        
        
    def display_account_info(self):
         print ("Your balance: $", self.balance)
  

        
    def yield_interest(self):
        if self.balance >= 0:
            self.interest = self.balance * self.int_rate
            self.balance = self.balance + self.interest


A001 = BankAccount()
A002 = BankAccount()
A003 = BankAccount()        

print ("=== Deposit Test ===")
A001.deposit (100)
A002.deposit (1000)

print ("=== Withdraw Test ===")
A001.withdraw (50)
A002.withdraw (500)
A003.withdraw (1000)

print ("===  Yield Interest Test ===")
A001.yield_interest ()
A002.yield_interest ()
A003.yield_interest ()

print ("===  Display Info Test ===")
A001.display_account_info ()
A002.display_account_info ()
A003.display_account_info ()