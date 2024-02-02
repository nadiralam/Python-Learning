# for loops works on range function and sequence 
for i in range(1,5):
    print(i)

for i in range(5):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(10,1,-1):
    print(i)  

number = int(input("enter the number:- "))
for i in range(1,11):
    n = number*i
    i+=1
    print(n)      

for i in "kolkata":
    print(i)

for i in [1,2,3,4,5]:
    print(i)  

# if we know about the repitation time in the loop then use for loops.LookupError.

# if the number of rotation time is finite then we use for loop in the code.

# Otherwise we use while loop in the code.