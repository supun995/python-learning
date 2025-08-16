import random

print("Welcome to guessing game!!!")

answer = random.randint(0,100)

def start_game(a):
    while True:
        guess = int(input("enter a number between 0-100 :"))
        if guess == a :
            print("WON")
            break
        elif guess < a:
            print("too small")
        else:
            print("TOO LARGE")

start_game(answer)



