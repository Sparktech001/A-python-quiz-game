import random

# A random guessing game using imported random module from python

lowest_num_guess = random.randint(5, 40)
highest_num_guess = (random.randint(1, 50))

# testing the randomness by changing the values

lowest_num = lowest_num_guess
highest_num = highest_num_guess

# I created random numbers for the values of the lowest and highest numbers

answer = random.randint(lowest_num, highest_num)
guesses = 0
print("---------PYTHON NUMBER GUESSING GAME-------")
print(f"Select a number between {lowest_num} and {highest_num}")
while True:
    guess = input("Enter your guess(q to quit): ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Pls select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low, try again")
        elif guess > answer:
            print("Too high, try again")
        elif guess == answer:
            print(f"CORRECT!! The answer was {answer}.")
            print(f"You tried for {guesses} times.")
            break
        else:
            break
    elif guess == "q":
        break
    else:
        print("INVALID GUESS")
        print(f"Select a number between {lowest_num} and {highest_num}")
"""This random number game runs by using the imported random module. it uses the while loop to loop those some conditions,
    it then prints the total number of trials after a successful game, it uses the break statment to escape the loop"""