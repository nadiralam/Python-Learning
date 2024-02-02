 # Operators are used to perform operations on variables and values.

# 1) Arithmetic operator(+,-,*,/,% **,//)

# 2) Comparision operaror(<,>,==,<=,>=)
x = 5; y = 6
print(x<y)
print(x>y)
print(x==y)
print(x<=y)
print(x>=y)

# 3) Logical operator(or ,not, and)
x = True
y = False
print(x or y)
print(not x)
print(not y)
print(x and y)
# 4) identity operator
h =5
j =5
print(h is j) # which means h and j are lies in same memory location 

a = [2,4,5]
b = [2,3,5]
print(a is b)
# 5) Assignment operator(=,+=,-+,*=,/=)
# 6) Bitwise operator
a = 5
b = 3
print(a&b)
print(a|b) 

print(a>>5)
print(b<<3)

#Membership Operator
z = "Nadir"
print("N" in z)

x = [1,3,4,5,6]
print(7 in x)