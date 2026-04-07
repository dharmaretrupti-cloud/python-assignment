import random
number = random.randint(1,50)
attempts = 5
while attempts > 0:
    guess = int(input("Guess the number between 1 and 50:"))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")    
    else:
        print("Yaaaaaaa!")