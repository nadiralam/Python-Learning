# list is a kind of data type which contains a multiple value in single variable is called list.
# list and array are fundamentally same but array contain homogeneous values.
# list contains non homogeneous values.
# it store all values in the square bricket.
# it doesn't store a value in a contiguous manner in a memory.

# Creating a list.
list = []
print(list)#----- empty list

list1 = [1,2,3,4,5]
print(list1)#----homogeneous list

list2 = [1,4,7,"nadir",'n']
print(list2) #---- heterogeneous list

# Multidimensional list.

list3 = [13,4,5,6,[6,8,9]]
print(list3)

list4 = [[[1,2],[3,4]],[[5,6],[7,8]]]
print(list4)

# Accessing if a list.
l1 = [1,3,4,5,6]
print(l1[0])
print(l1[-1])
print(l1[1:3])
print(l1[1:5:3])
print(l1[::-1])

list3 = [13,4,5,6,[6,8,9]]
print(list3[-1])
x = list3[-1]
print(x[0])
print(x[1])
print(x[2])
#------------ or---------
list3 = [13,4,5,6,[6,8,9]]
print(list3[-1][0])


list4 = [[[1,2],[3,4]],[[5,6],[7,8]]]
print(list4[-1][-1][0])
print(list4[0][1][1])

# Editing a list.
list6 = [3,5,7,8]
print(list6)
list6[0] = "nadir" 
print(list6) #----- because list are mutable.
list6[0:] = [100,200,300,400]
print(list6)

# Adding a list.
# there are three types of adding in a list 
# 1) append
# 2) extend
# 3) insert

#Append(add single items at last in a list)
list7 = [100,300,500,700,800]
list7.append(1000)
list7.append("world")
print(list7)

# Extend( add multiple items at last in a list)
list7 = [100,300,500,700,800]
list7.extend([2000,4000,6000,"nadir"])
print(list7)

# Insert.
list7 = [100,300,500,700,800]
list7.insert(1,50)
print(list7)

# Delete in a list.
# there are four types to delete a list 
# 1) del
# 2) remove
# 3) pop
# 4) clear

# del( whole list is deleted)
list8 = [20,30,40,50,60,70]
# del list8 
# print(list8)

del list8[0]
del list8[-5]
print(list8)

# Remove( it delete element of list from desire location)
list8 = [20,30,40,50,60,70]
list8.remove(50)
print(list8)

# Pop(it delete one element of list from last)
list8 = [20,30,40,50,60,70]
list8.pop()
print(list8)
list8.pop()
print(list8)
list8.pop()
print(list8)

# claer( it works to empty the list)
list8 = [20,30,40,50,60,70]
list8.clear()
print(list8)

# Operation on list.
l1 = [5,6,7,8]
l2 = [10,20,49]
print(l1+l2) #------ concatenation

l1 = [5,6,7,8]
print(l1*3)

l3 = [5,6,7,18]
for i in l3:
    print(i)

for i in l3:
    print(l3) 

l3 = [5,6,7,18] 
print(6 in l3)  #----- membership operator
print(4 in l3)

# Functiions of list
l4 = [5,2,1,8,6]
print(len(l4))
print(max(l4))
print(min(l4))
print(sorted(l4)) # it not change the original list but it create new list
print(sorted(l4,reverse = -1))

l4.sort()
print(l4) # it change the original list permanently.