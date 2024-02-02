# it is just similar to the list but one difference is list is mutable and tuple is immutable.
# it is denoted by small bricket.

# Creating a tuple.
tuple = ()
print(tuple)

tuple1 = (1,2,3,4,5,6)
print(tuple1) # ---- homogeneous tuple

tuple2 = (1,3,6,8,"Delhi",'N')
print(tuple2) # --- heterogeneous tuple

# 2-D tuple
t1 = (1,3,5,6,(7,9))
print(t1)

tuple3 = (3)
print(tuple3)
print(type(tuple3)) #----- not a tuple

# single item tuple
t2 = ('hello',)
print(t2)
print(type(t2))

# Accessing a tuple.
t1 =  (1,3,5,6,(7,9))
print(t1[0])
print(t1[-1])
print(t1[-1][0])
print(t1[0:5:3])

print(t1[0:])
print(t1[:-1])
print(t1[::-1])

# Editing a tuple
# t1 = (1,3,5,6,(7,9))
# t1[0] = 100
# print(t1)

# We cann't edit the tuple because it immutable in nature.
# We cann't add values in the original tuple because it is immutable.

# Deleting in tuple.
t1 = (1,3,5,6,(7,9))
del(t1)
# print(t1)

# We delete the tuple completely. And not delete partially.
# Because tuple are immutable( not changeble).


# OPERATIONS IN TUPLE.

t1 = (1,3,5,6,(7,9))
t2 = ('hello',)
print(t1+t2) #----- concatenation in tuple

t2 = ('hello',)
print(t2*3)

for i in t1:
    print(i)

for i in t2:
    print(i)

t2 = ('hello',)
print('hello' in t2)
t1 = (1,3,5,6,(7,9))
print(5 in t1)
print(9 in t1) #--------- membership operator

# FUNCTIONS IN TUPLE.

t3 = (1,3,5,6,9)
print(len(t3))
print(max(t3))
print(min(t3))
print(sum(t3))
print(sorted(t3))
print(sorted(t3,reverse = True))
print(sorted(t3,reverse = -1))

# tuples are read only data type.
# not write only data type.