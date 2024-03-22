# Once again learning the python by Mosh 
print('Saqib '  * 10)

# lets now do some exercises 

#patient_name = "Saqib Bedar "
#age = '19'
#is_new = True
#print(patient_name + age )
#print(is_new)

# How to take input from a user using Python 

#name = input('What is your name?')
#print("Hello " + name )
#ask_more = input("How are doing?")
#print("That sounds good that you are " + ask_more)
#third_question = input ("How can I help you " + name + "?")

# Exercise by Mosh - Two questions

#full_name = input (" What is your full name?")
#fav_color = input ("What is favorite color?")
#print ( full_name + " likes " + fav_color)

# Calculate your age Python 

# birth_year = input ("Birth Year")
# age= 2023 - int (birth_year)

# def getAge():
#     birth_year = input("Enter your birth year: ")
#     return 2024 - int(birth_year)


# print("You are", getAge(), "years old!")

def main():
    age = int(input("What's your birth year? "))
    age = 2024 - age
    getAge(age)

def getAge(age):
    print(f"You are {age} years old!")

main()