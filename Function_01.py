# CREATING A FUNCTION

def first_pgm():
    print("hello, world!")

first_pgm()

# CALLING A FINCTION
def my_function():
  print("Hello from a function")

my_function()
# or

def py():
   for i in range(1,11):
      for j in range(1, i+1):
        print("*", end = "")
      print()
   
py()

def sum(a,b):
   c = a+b
   return c

x = sum(10,5)
print("the sum is:- ",x )
y = sum(5478923,674980548)
print("the sum is:- ",y )

# PARAMETERS VS ARGUMENTS.
# 1) DEFAULT ARGUMENTS

def power(a = 1,b = 1):
   return a**b

print(power(2,3))
print(power(3,4))
print(power(5))
print(power())

# here is default value is one.

# 2) POSITIONAL ARGUMENTS
def power(a,b):
   return a**b

print(power(2,3))
print(power(3,4))
# print(power(5)) #---- positional arguments(one value is missing).

# 3) KEYWORD ARGUMENTS
def power(a = 1,b = 1):
   return a**b

print(power(2,3))
print(power(b = 2,a = 3)) #--- keyword argument.

# # 4) ARBITRARY ARGUMENTS

# print(1,2,3,4,5)

def flexi(*number):
   product = 1
   print(number)
   print(type(number))
   for i in number:
      product = product*i
   print(product)

flexi(1,2,3,4,5)
flexi(6,7,8,9)

# NESTED FUNCTIONS.

def f():
   print("inside f")
   def g():
      print("inside g")

   g()
  
f()  

# nested function is hidden from main program.
# f() is not know about g().

def g(x):
   def h(x):
      x = x+1
      print("in h(x): x = ",x)
   x = x+1
   print("in g(x): x = ", x)
   h(x)
   return x

x = 3
z = g(x)
print("in main program scope: x= ",x)
print("in main program scope: z= ",z)

# FUNCTIONS AS OBJECTS IN PYTHON
def f(num):
   return num**2

print(f(2))
print(f(4))
print(f(8))

x = f
print(x(2))
print(x(4))
print(x(8))
print(type(x))

del f
# print(f(2))
print(x(2))