# LAMDA FUNCTION.

x = lambda x: x**2
print(x(4))

a = lambda x,y: x+y
print(a(43,6))

# DIFFERENCE FROM NORMAL FUNCTION.

# 1) lambda has no return value.
# 2) one line function.
# 2) not used for code reusability.
# 4) it has no name function.

b = lambda x: x[0]=="a"
print(b("apple"))
print(b("kolkata"))
 
c = lambda x: "even" if x%2== 0 else "odd"
print(c(3))
print(c(4))

# Lambda functions are used in higher order function.

def return_sum(func,L):
    result = 0
    for i in L:
        if func(i):
            result = result+i
    return result
    
L = [11,14,21,23,56,78,45,29,28]

x = lambda x: x%2==0
y = lambda x: x%2!=0
z = lambda x: x%3==0

print(return_sum(x,L))
print(return_sum(y,L))
print(return_sum(z,L))

# MAP FUNCTION
l1 = [2,3,4,58,9,45]
print(map(lambda x: x*2,l1))

list(map(lambda x: x*2,l1))
print(list(map(lambda x: x*2,l1)))

list(map(lambda x: x%2==0,l1))
print(list(map(lambda x: x%2==0,l1)))

students = [
            {"name":"nadir","age":20,"G":"male",},
            {"name":"siraj","age":21,"G":"female",},
            {"name":"Nandini","age":19,"G":"male",}
            ]
map(lambda student: student["name"],students)
print(map(lambda student: student["name"],students))

list(map(lambda student: student["name"],students))
print(list(map(lambda student: student["name"],students)))

# ------------------FILTER--------------------.

L2 = [2,3,4,5,6,7,8]
filter(lambda x: x>4,L2)
print(filter(lambda x: x>4,L2))

list(filter(lambda x: x>4,L2))
print(list(filter(lambda x: x>4,L2)))

l3 = ['apple','orange','mango','guava']
filter(lambda l3: 'e' in l3,l3)
print(list(filter(lambda fruit: 'e'in l3,l3)))

# REDUCE------------------------------->

import functools
L2 = [2,3,4,5,6,7,8]
functools.reduce(lambda x,y: x+y,L2)
print(functools.reduce(lambda x,y: x+y,L2))

