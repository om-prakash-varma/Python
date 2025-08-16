n = int(input("Enter the number: "))
rv = 0
while n > 0:
    r = n%10
    rv = rv*10+r
    n = n//10

print("REVERSE NUMBER: ",rv)
