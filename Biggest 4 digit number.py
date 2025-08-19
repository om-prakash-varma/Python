n1 = int (input("Eenter the First Number:"))
n2 = int (input("Eenter the Second Number:"))
n3 = int (input("Eenter the Third Number:"))
n4 = int (input("Eenter the Forth Number:"))

if ((n1 > n2) & (n1 > n3) & (n1 > n4)):
    print ("Biggest Number is :",n1)
elif ((n2 > n3 ) & (n2 > n4)):
      print ("Biggest Nuber is :",n2)
elif (n3 > n4):
    print ("Biggest Number is :",n3)
else:
    print ("Biggest Number is :",n4)
