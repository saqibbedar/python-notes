# round(number[, ndigits]): round is a function and it has first argument number and [ this symbol represents in documentation it is optional and then there is second argument which is ndigigts that use for how many numbers you want to round-off


x = float(input("What's x? ")) # 999
y = float(input("What's y? ")) # 1

z = round(x+y) # 1000

print(z) # 1000

print(f"{z:,}") # using :, for formatting number like 1000 to 1,000 so output will be 1,000 

a = float(input("Enter a's value: "))
b = float(input("Enter b's value: "))

c = round(x/y, 2) 
# Or I can format it: f"{z:.2f}", this expression is equivalent to the round(x/y, 2)

print(f"{c}")