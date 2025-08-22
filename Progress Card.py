st_name = (input("Enter your name:"))
ht_no = int (input("Enter your Hall Ticket Number:"))
sub_1 = int (input("Enter marks obtained in Maths:"))
sub_2 = int (input("Enter marks obtained in Englis:"))
sub_3 = int (input("Enter marks obtained in Science:"))
sub_4 = int (input("Enter marks obtained in Social:"))
sub_5 = int (input("Enter marks obtained in Telug:"))

print ("                                             ")
print ("                                             ")
print ("---------------- STUDENT PROGRESS CARD ----------------")
print ("                                                       ")
print ("NAME OF THE STUDENT: ",st_name)
print ("HALL TICKET NUMBER : ",ht_no)
print ("                                                       ")
print ("SUBJECT       RESULT    MARKS ")
if sub_1 >= 35:
    print ("MATHS    :    PASS    :",sub_1)
else:
    print ("MATHS    :    FAIL    :",sub_1)

if sub_2 >= 35:
    print ("ENGLISH  :    PASS    :",sub_2)
else:
    print ("ENGLISH  :    FAIL    :",sub_2)

if sub_3 >= 35:
    print ("SCIENCE  :    PASS    :",sub_3)
else:
    print ("SCIENCE  :    FAIL    :",sub_3)

if sub_4 >= 35:
    print ("SOCIAL   :    PASS    :",sub_4)
else:
    print ("SOCIAL   :    FAIL    :",sub_4)

if sub_5 >= 35:
    print ("TELUGU   :    PASS    :",sub_5)
else:
    print ("TELUGU   :    FAIL    :",sub_5)

print ("            ")

tl_mrk = sub_1 + sub_2 + sub_3 + sub_4 + sub_5

print ("             TOTAL MARKS:",tl_mrk)

if tl_mrk >= 35*5:
    print ("             OVERALL RESULT: PASS")
else:
    print ("             OVERALL RESULT: FAIL")

avg = tl_mrk/50

print ("             AVERAGE POINTS:",avg)
print ("                                                      ")
t2_mrk = tl_mrk/5
if t2_mrk >= 90:
    print ("GRADE   : A+,  PERCENTAGE:",t2_mrk)
    print ("REMARKS : EXCELLENT")
elif t2_mrk >= 80:
    print ("GRADE   : A,  PERCENTAGE:",t2_mrk)
    print ("REMARKS : VERY GOOD")
elif t2_mrk >= 70:
    print ("GRADE   : B+,  PERCENTAGE:",t2_mrk)
    print ("REMARKS : GOOD")
elif t2_mrk >= 60:
    print ("GRADE   : B,  PERCENTAGE:",t2_mrk)
    print ("REMARKS : KEEPIT-UP")
elif t2_mrk >= 45:
    print ("GRADE   : C+,  PERCENTAGE:",t2_mrk)
    print ("REMARKS : NEED TO IMPROVE")
elif t2_mrk >= 35:
    print ("GRADE   : C,  PERCENTAGE:",t2_mrk)
    print ("REMARKS : NEED TO IMPROVE")
else:
    print ("RESULT : FAIL")
    print ("REMARKS : BETTER LUCK NEXT TIME")

print("-------------------------------------------------------")
