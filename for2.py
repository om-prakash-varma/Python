n1 = int(input("Enter the value of number-1: "))
n2 = int(input("Enter the value of number-2: "))

if n1 < n2:
    for i in range(n1,n2+1):
        print(i)
else :
    for i in range(n1,n2-1,-1):
        print(i)
