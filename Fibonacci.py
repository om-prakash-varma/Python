r = int (input("Enter range: "))

n1 = 0
n2 = 1

print (n1,n2, end= " ")
n3 = n1 + n2

while n3 <= r:
    print (n3, end=" ")
    n1 = n2
    n2 = n3
    n3 = n1 + n2
