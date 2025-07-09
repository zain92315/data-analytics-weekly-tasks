import random

print("Number guessing game")
try:
    lower=int(input("Enter lower bound"))
    upper=int(input("Enter upper bound"))
    if lower >= upper:
        raise ValueError("lower bound must be greater than upper bound")
except ValueError  as ve:
    print(f"error:{ve}")
    
number = random.randint(lower,upper)  
attempts=0
print(f"Guess a number between {lower} and {upper}")
while True:
    try:
        guess=int(input("your guess: "))
        attempts+=1
        if guess < number:
            print("Higher")
        elif guess > number:
            print("Lower")
        else:
            print(f"you guessed number in {attempts} Attempts")
            break
    except Exception as e:
        print(f"error: {e}")
        
