class BankAccount:
  def __init__(self, account_number, balance)
  self.__account_number = 0
  self.__balance = 0.0
  self.set_balance(balance)
  self.set_account_number(account_number)

  def set_account_number(self, number):
    self.account_number = number

def set_balance(self, amount):
  if amount > 0:
    self.balance = amount
  else:
    print("The balance must not be negative!")

  @property
    def account_number(self):
      return self.__account_number
  
  @property
    def balance(self):
      return self.__balance

  a1 = BankAccount(12345, 1000)
  print("Account 1")
  print(f"Account Number: {my_account.account_number}")
  print(f"Balance: {a1.balance: .2f}")
  
  

  
