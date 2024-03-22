def main():
    name = input("What's your name? ").title().strip()
    hello(name)

def hello(to = "world"):
    print("Hello,", to)
 
main()