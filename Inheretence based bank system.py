#parent class
class User:
  def __init__(self,name,age,gender):
    self.name=name
    self.age=age  
    self.gender=gender
  def show_details(self):
    print("Personal Details..")
    print()
    print( f'Name: {self.name}\nGender: {self.gender}\nAge: {self.age}')
    print()


class Bank(User):
  def __init__(self,name,age,gender):
    super().__init__(name,age,gender)
    self.balance= 0
  def deposit(self,amount):
    self.balance += amount
    print(f'Account Balance has been updated : $ {self.balance}.')
    
  def withdraw(self,amount):
    if amount > self.balance:
      print(f"Insufficient Balance ! \nBalance Available: ${self.balance} \nIn-Order to Withdraw kindly recharge your account. ")
    else:
      self.balance -= amount
      print(f'Amount Withdrawn: ${amount}.\nYour remaining balance is: $ {self.balance}')
      
  def view_balance(self):
    print(f'Current Balance in your Account: $ {self.balance}')
    
user=Bank('Khayyam',15,'Male')
print()
user.show_details()
print()
print(user.name)
print()
print(user.age)
print()
print(user.gender)
print()
user.view_balance()
print()
user.deposit(1000)
print()
user.view_balance()
print()
user.withdraw(455)
print()
user.deposit(1500)
print()
user.withdraw(2500)
print()
user.view_balance()