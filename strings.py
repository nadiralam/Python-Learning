# it is a application programming language.
# string is a sequence of character.
# In python ,strings are a sequence of Unicode character.

# Creating
a = "hello"
print(a)

c = 'nadir'
print(c)

d = '''Welcome to the bhopal'''
print(d)

e = """kolkata"""
print(e)

f = str("hello")
print(f)

# Acessing a substring from a string.
#Indexing

a = "Delhi"
print(a[4])

# there are two types of indexing(Positive Indexing,Negative Indexing)

c = 'nadir'
print(c[-5])

# Sciling.
b = "Good Morning!"
print(b[0:4])
print(b[2:])
print(b[:7])
print(b[:])
print(b[0:10:3])
print(b[-5:-1:2])

# reversing 

print(b[::-1])
print(b[-1:-6:-1])

# Editing and Deleting a string.
# g = "good"
# g[0] = 'm'
# print(g[0])

# We are cannot edit the string because it is a immutable data type.
# we cannot change the string
# we cannot add the characters
# we cannot delete string partially.
#we can assign the string
g = "good"
g = "mood"
print(g)

#DELETING
del g
print(g)

