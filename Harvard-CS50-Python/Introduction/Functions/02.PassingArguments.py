# say hello to user by taking an argument
def say_Hello(to):
    # user = to.strip().title() 
    print(f"Hello, {to}")

name = input("What's your name? ").strip().title()
say_Hello(name)


# if user has not pass an argument then function should use its default parameter
def hello(to = "world"):
    print("Hello,", to)

hello()