def main():
     x = int(input("What's x? "))
     print(f"{x} squared is", square(x))

def square(n):
    return n*n # or I can use n**2 or we can use pow(n, 2)

main()