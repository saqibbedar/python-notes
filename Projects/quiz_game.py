print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! let's play :) ")

answer = input("What is CPU stands for? ").title()

if answer == "Central Processing Unit":
    print("Correct!")
else: 
    print("Incorrect!")

# create some other questions