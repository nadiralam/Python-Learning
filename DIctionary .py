dict = {"name":"nadir","gender":"male"}
print(dict)

# Dictionary contains some rules
# 1) it has no indexing.
# 2) it is a mutable data types
# 3) keys-> immutable,values can be mutable.
# 4) keys should be unique.

# Mutable-> list,set,Dictionary
# Immutable-> strings,tuples,int,float,boolean,complex


#CREATING A DICTIONARY.
d = {}
print(d)
print(type(d)) #------empty dictionary.

d1 = {"name":"nadir","gender":"male","age":20}
print(d1)

# d3 = {[1,2,3,4]: "hello"}
# print(d3) #---------not possible because keys are immutable.

d4 = {(1,2,3,4,5):"Delhi"}
print(d4)
print(type(d4))

# Dictionary keys contains recent values.

d5 = {"name":"nadir","college":"oist","marks":{"m1":56,"ds":66,"eng":89}}
print(d5)

#ACCESSING ITEMS FROM A DICTIONARY.
d1 = {"name":"nadir","gender":"male","age":20}
print(d1["name"])
print(d1["gender"])
print(d1["age"])

d5 = {"name":"nadir","college":"oist","marks":{"m1":56,"ds":66,"eng":89}}
print(d5["marks"]["ds"]) # ---- accessing 2-d dictionary.


# print(d1[0]) --- not possible in dictionary


# Editing a dictionary

d5 = {"name":"nadir","college":"oist","marks":{"m1":56,"ds":66,"eng":89}}
d5["name"] = "Rahul"
print(d5)

d5["college"] = "tit"
print(d5)

d5["marks"]["ds"] = 88
print(d5)

# ADDING NEW VALUE IN A DICTIONARY.
d5 = {"name":"nadir","college":"oist","marks":{"m1":56,"ds":66,"eng":89}}
d5["age"] = 21
print(d5)

d5["marks"]["hindi"] = 78
print(d5)

# DELETING A VALUE FROM DICTIONARY.
d5 = {"name":"nadir","college":"oist","marks":{"m1":56,"ds":66,"eng":89}}
# del d5
# print(d5)

del d5["marks"]
print(d5)

d5.clear()
print(d5)

# OPERATIONS

# Concatenation is not occur in dictionary(d1+ d2 = not possible).

d5 = {"name":"nadir","college":"oist","marks":{"m1":56,"ds":66,"eng":89}}
for i in d5:
    print(i)

d4 = {(1,2,3,4,5):"Delhi"}
for i in d4:
    print(i,d4[i])

d4 = {(1,2,3,4,5):"Delhi"}
print("Delhi" in d4)

print("marks" in d5)

# FUNCTION OF DICTIONARY USED.
d4 = {(1,2,3,4,5):"Delhi"}
print(len(d4))
print(max(d4))
print(min(d4))
print(sorted(d4))
print(sorted(d4, reverse = True))

d5 = {"name":"nadir","college":"oist","marks":{"m1":56,"ds":66,"eng":89}}
print(len(d5))
print(max(d5))
print(min(d5))
print(sorted(d5))
print(sorted(d5, reverse = True))

