# We are using super keyword for accessing the parent class attribute.
# It can't be used outsidethe class
# We are generally use inside the child class.
# It can access the methods of the class not the attributes of the class.


class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        print(self.__price)

        self.brand = brand
        print(self.brand)

        self.camera = camera
        print(self.camera)

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        # syntax to call parent ka buy method
        super().buy()

s=SmartPhone(20000, "Apple", 13)

s.buy()

# Example 2.

class Parent:

    def __init__(self,num):
      self.__num=num

    def get_num(self):
      return self.__num

class Child(Parent):
  
    def __init__(self,num,val):
      super().__init__(num)
      self.__val=val

    def get_val(self):
      return self.__val
      
son=Child(100,200)
print(son.get_num())
print(son.get_val())

# Example 3.

class Parent:
    def __init__(self):
        self.num=100

class Child(Parent):

    def __init__(self):
        super().__init__()
        self.var=200
        
    def show(self):
        print(self.num)
        print(self.var)

son=Child()
son.show()

# Example 4.
class Parent:
    def __init__(self):
        self.__num=100

    def show(self):
        print("Parent:",self.__num)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var=10

    def show(self):
        print("Child:",self.__var)

obj=Child()
obj.show()

