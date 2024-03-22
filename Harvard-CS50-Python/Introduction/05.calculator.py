# get values from user
x = int(input("Enter value: "))
sign = input("Enter symbol: ")
y = int(input("Enter value: "))

# print the result: match is same like switch in other programming languages
match sign:
    case '+':
        print(f"{x} + {y} = ", x+y)
    case '-':
        print(f"{x} - {y} = ", x-y)
    case '*':
        print(f"{x} * {y} = ", x*y)
    case '/':
        print(f"{x} / {y} = ", x/y)
    case _:
        print("Invalid symbol")

        