"""student_attendece=76
marks=90
if student_attendece >= 75:
    if marks >=40:
        print("eliguble and pass")
    else:
        print("eligible but fail")
else:
    print("not eligible")



purchase_amount=int(input("enter the purchase amount: "))
coustmer=input("are you a coustmer? (yes/no): ")
if coustmer=="yes":
    if purchase_amount>=25000:
        print("discount 25%")
    else :
        print("discount 10%")
else :
    if purchase_amount>25000:
        print("discount 10%")
    else:
        print("no discount")"""


marks1=int(input("entre your marks:"))
if marks1>=40:
    if marks1>=75:
        print("distinction")
    else:
        print("pass")
else:
    print("fail")


letter=input("enter the letter:")
if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u" or letter=="A" or letter=="E" or letter=="I" or letter=="O" or letter=="U":
    print("vowel")
else:
    print("consonant")

list=("a","e","i","o","u","A","E","I","O","U")
letter1=input("enter the letter:")
if letter1 in list:
    print("vowel")
else:
    print("consonant")





candidate=input("enter degree")
if candidate=="yes":
    experience=int(input("do you have experience?  "))
    if experience==2:
        print("eligible for interview")
    else:
        print("freshers for interview")
else:
    print("not eligible for interview")

