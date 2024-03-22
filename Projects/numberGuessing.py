import random

# ran_num = random_number
ran_num = random.randint(0,11) #randrange(-5, 10) || randint(-5, 11) etc

guess = input("Guess a number between 0 to 11: ")

#check if number is is digit or not?
if guess.isdigit(): 
    guess = int(guess)
else:
    # if not a integer then throw error message
    print("Error: you entered string!")
    quit()

if guess == ran_num:
    print("Correct!")
else:
    print("Incorrect!")