# sets donot allow duplicate value.
# sets have no idexing/slicing
# sets don't allow mutable data type
# sets itself is a mutable data type
# multi dimensional data type are not allowed.
 
# CREATING A SETS.
set = {}
print(set) 
print(type(set)) # --- it is a dictionary not a set.

set1 = {1,2,3,4,6,9}
print(set1)
print(type(set1)) #----- homogeneous set.

set2 = {1,2,4,6,'jhansi','N'}
print(set2)
print(type(set2)) # -----heterogeneous set.
# sets follows hashing. not indexing.

# donot allow duplicates
s1 = {1,1,2,2,3,3}
print(s1)

# donot allow mutable.
# s2 = {[1,2,3],"hello"}----- not possible because list is mutable.
# print(s2)

s3 = {(1,2,3,4),"hello"}
print(s3) #----- it is possible because tuple is immutable.

# Accessing a sets.
# s4 = {1,2,3,4,5,6}
# print(s4[0]) --- sets donot allow aceessing a set.

# We cann't edit a set.

# Adding a set.
s4 = {1,2,3,4,5,6}
s4.add(9)
x = id(s4)
print(s4)
print (x)

s4.add(18)
print(s4)
print (x)

# Delete element from set
# 1) del

s4 = {1,2,3,4,5,6}
del s4
# print(s4)

# 2) remove
s4 = {1,2,3,4,5,6}
s4.remove(4)
print(s4)

s4.remove(6)
print(s4)


# 3) pop
s4 = {1,2,3,4,5,6}
s4.pop()
print(s4)

s4.pop()
print(s4)

# OPERATIONS ON SETS
# We cann't concatinate the sets( s1+s2  = not possible.)

s4 = {1,2,3,4,5,6}
for i in s4:
    print(i)

s4 = {1,2,3,4,5,6}
print(5 in s4)
print( 10 in s4)   #---- membership operation.

# FUNCTION OF SETS.

s4 = {1,2,3,4,5,6}
print(len(s4))
print(max(s4))
print(min(s4))
print(sum(s4))
print(sorted(s4))
print(sorted(s4, reverse = True))
print(sorted(s4, reverse = -1))



# some other function 
s5 = {1,3,4,5}
s6 = {5,7,9,5}
y = s5.union(s6)
print(y)

s5 = {1,3,4,5}
s6 = {5,7,9,5}
z = s5.intersection(s6)
print(z)

s5 = {1,3,4,5}
s6 = {5,7,9,5}
z = s5.difference(s6)
print(z)

s5 = {1,3,4,5}
s6 = {5,7,9,5}
z = s6.difference(s5)
print(z)

s5 = {1,3,4,5}
s6 = {5,7,9,5}
z = s5.symmetric_difference(s6)
print(z)

s5 = {1,3,4,5}
s6 = {5,7,9,5}
z = s5.isdisjoint(s6)
print(z)

s5 = {1,3,4,5}
s6 = {5,7,9,5}
z = s5.issubset(s6)
print(z)

s5 = {1,3,4,5}
s6 = {5,7,9,5}
z = s5.issuperset(s6)
print(z)