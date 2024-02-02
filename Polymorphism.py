# Method Overriding

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

s=SmartPhone(20000, "Apple", 13)

s.buy()
# Method Overloading

class Shape:

  def area(self,a,b=0):
    if b == 0:
      return 3.14*a*a
    else:
      return a*b

s = Shape()

print(s.area(2))
print(s.area(3,4))

# Generally are not using method overloading in python because the intrepreter doesn't find which one be executed first.

# Operator Overloading

