# QUESTION NO:- 1
sample = "how are you?"

print(sample.split())

l = []
for i in sample.split():
    print(i.capitalize())
    l.append(i.capitalize())

print(l)
print(" ".join(l))


# QUESTION NO:- 2
sample = "today has been great for me."

print(sample.split())

l1 = []
for i in sample.split():
    print(i.capitalize())
    l1.append(i.capitalize())

print(l1)
print(" ".join(l1))

# QUESTION NO:- 3

l2 = "abc@gmail.com"
print(l2[0:3])

# question no:- 4
l3 = [1,1,2,2,3,3,4,4]

l =[]
for i in l3:
    if i not in l:
        l.append(i)
print(l)

l =[]
for i in l3:
    if i not in l:
        l.append(i)
print(l)