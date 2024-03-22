x = int(input("what's x? "))
y = int(input("what's y? "))

if x < y:
    print(f"{x} is less than {y}")
elif x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} and {y} are equal")