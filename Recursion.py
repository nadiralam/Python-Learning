# it is a process in which a function calls itself directly or indirectly. 
# A complicated function can be split down into smaller sub-problems utilizing recursion.
# Sequence creation is simpler through recursion than utilizing any nested iteration.
# Recursive functions render the code look simple and effective.

# multiply7ing of two number using recursion.

def mul(a,b):
    if b==1:
        return a
    else:
        return a+mul(a,b-1)
print(mul(3,4))

def mul(c,d):
    if d==1:
        return c
    else:
        return c+mul(c,d-1)
    
print(mul(5,6))

# FACTORIAL OF A GIVEN NUMBER.

def fact(number):
    if number==1:
        return 1
    else:
        return number *fact(number-1)
    
print(fact(10))
print(type(fact))

# palindrome code.

def palin(string):
    if len(string)<=1:
        print("palindrome")
    else:
        if string[0]== string[-1]:
            palin(string[1:-1])
        else:
            print("not a palindrome")

            
print(palin("madam"))
print(palin("malayalam"))
print("python")
print(palin("abba"))

# THE RABBIT PROBLEM(FABINACCI SERIES).

def fib(month):
    if month == 0 or month==1:
        return 1
    else:
        return fib(month-1) + fib(month-2)
    
print(fib(12))


# Reduce time of fibonacci series through memorization in dynamic programming.

def memo(m,d):
    if m in d:
        return d[m]
    else:
        d[m] = memo(m-1,d)+ memo(m-2,d)
        return d[m]
    
d = {0:1,1:1}
print(memo(48,d)) 
print(memo(100,d)) 
print(memo(500,d))   
