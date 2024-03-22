# str is a datatype in python and it has many built-in functions some of them we will use here

# ask user for their name
name = input("Enter your name? ")

# strip(): it is method that removes whitespaces from str, it return a copy of the string with leading and trailing whitespace removed
name = name.strip()

# Capitalize user name
name = name.capitalize() # capitalize method will only make capital to the first letter in string not other words so thats we use some other function title() to capitalize each first letter of the word

# string formatting
value = f"hello, {name}"

# say hello to the user
print(value) 

value = value.title()

print(value) 


# Optimizing the code 
user = input("Enter your name? ").strip().title()

# Say hello to user
print(f"Hello, {user}")