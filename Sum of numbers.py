n = int(input("Enter teh number: "))
sm = 0
while n > 0:
    r = n%10
    sm += r
    n = n//10

print (sm)
