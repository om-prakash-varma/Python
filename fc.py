nd = int(input("Enter number of digits: "))
np = int(input("Enter the posetion of the number need to be printed: "))

n1 = 0
n2 = 1
cn = 2

print (n1,n2,end=" ")
n3 = n1 + n2

while cn < nd:
    print (n3, end= " ")
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    cn += 1
    if np==cn:
        print (n3)
