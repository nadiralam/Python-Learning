import random
jackpot = random.randint(1,100)
guess = int(input("enter the number:- "))
counter = 1
while guess!= jackpot:
    if guess < jackpot:
        print("guess higher")
    else:
        print("guess lower")

    guess = int(input("enter the number:- "))
    counter+=1
print("correct answer")
print("you attempt", counter)