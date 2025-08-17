n = int (input("Enter the number"))

sm = 0

while n > 0:
    r = n % 10
    if r % 2 == 0:
        sm += r**2
    else:
        sm +=r**3
    n = n//10
print (sm)
