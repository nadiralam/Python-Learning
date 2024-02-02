print("hello world")

# the conversion of one data type is into another data type is known as typecasting.


a  = "1"
# a = 1

b = "2"
# b = 2

print(int(a)+int(b))

# print(a+b)


# There are two type of typeCasting in python
# 1) Explicit typeCasting( doing by user)

# this typeCasting contain some function such as int(),float(),hex(),oct(),str()etc.
# Example

string = "57"
number = 6
string_number = int(string)

sum = string_number + number
print(sum)
# 2) Implicit typeCasting(doing by python itself)
# Example

a = 6
print(a)
print(type(a))

b = 78.4
print(b)
print(type(b))

c = a+b
print(c)
print(type(c))