import random
number=random.randint(1,9)
print("Guess a Number between 1-9")
chance=0
while chance<5:
    guess=int(input("Enter your number:  "))
    if guess==number:
            print("Congratulations you won")
            break
    elif guess<number:
            print("Your guess was too low")
    else:
            print("Your guess was too high")
    chance=chance+1
if not chance<5:
    print("You lose")