course = "Python for Beginners "

# print (course)
getDigit = int(input("What's digit? "))

def getChar(digit):
    courseLength = len(course)
    return course[digit] if digit <= courseLength else "out of bound"

print(getChar(getDigit))