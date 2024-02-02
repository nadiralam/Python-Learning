# Every thing in python is consider as object.
# oop consist of several principal.
# 1) class
# 2) object
# 3) abstraction
# 4) Encapsulation
# 5) inheritance
# 6) polymorphism

# CLASS.

# Class is a blue print of his object and it identifies how the objects works
# Class is a set of rule and it is followed by objects.
# there are two types of classes in python.
# 1) built in classes.
# 2) user defined claees.

# syntax:

# class Car:
#    color = "blue"
#    model = "sports"
#    def calculate_avg_speed(km,time):
#       # code

#OBJECT.

# objects is an instance of the class
# examples.

# car--------------wagonR--------wagonr = car()
# sports-----------cricket--------cricket = sports()
# Animals----------elephant--------elephant = Animal()

# syntax:

#ibjectname = classname().


class Atm:

  # constructor(special function)->superpower -> 
  def __init__(self):
    # print(id(self))
    self.pin = ''
    self.balance = 0
    self.menu()

  def menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
    elif user_input == '4':
      self.withdraw()
    else:
      exit()

  def create_pin(self):
    user_pin = input('enter your pin')
    self.pin = user_pin

    user_balance = int(input('enter balance'))
    self.balance = user_balance

    print('pin created successfully')
    self.menu()

  def change_pin(self):
    old_pin = input('enter old pin')

    if old_pin == self.pin:
      # let him change the pin
      new_pin = input('enter new pin')
      self.pin = new_pin
      print('pin change successful')
      self.menu()
    else:
      print('nai karne de sakta re baba')
      self.menu()

  def check_balance(self):
    user_pin = input('enter your pin')
    if user_pin == self.pin:
      print('your balance is ',self.balance)
    else:
      print('chal nikal yahan se')

  def withdraw(self):
    user_pin = input('enter the pin')
    if user_pin == self.pin:
      # allow to withdraw
      amount = int(input('enter the amount'))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print('withdrawl successful.balance is',self.balance)
      else:
        print('abe garib')
    else:
      print('sale chor')
    self.menu()

obj = Atm()



# A finction lies inside the class is called method.
# A function lies outside the class then it is known as function.

# self

# self is a default parameter

# CONSTRUCTOR

# there are two types.
# 1) parametrized constructor(it contains input for creating a objects)
# 2) non parametrized constructor(it doen't contains input during creating a objects)

# MAGIC METHOD:-

# it is a denoted by __name__.
# it has a super power.
# constructoris is a magic method.

# Some other magic methods are:-

# 1) __init__
# 2)__str__(showing the values of object)
# 3)__add__(add two ojects)
# 4)__sub__(substract two object)
#5)__mul__(multiply b/w two objects)
#6)__div__(divide two objects)