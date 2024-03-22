'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
'''

def triangle():
    size = int(input("Enter rows: "))
    for i in range(0, size+1):
        for j in range(0, i+1):
            print("*", end=" ") 
        print()

triangle()