temp=40
current_wether =41

if temp < current_wether:
     print("high temperature")
else:
    print("low temperature")


num =int(input("enter a number: "))
num%2==0            
if num%2==0:
    print("even number")
else:
    print("odd number")


marks=75
if marks >= 90:
    print("A grade")    
elif marks >= 80:
    print("B grade")
elif marks >= 70:
    print("C grade")
else:
    print("Fail")


num=int(input("enter a number: "))
if num==1:
    print("balance")
elif num==2:
    print("withdraw")
elif num==3:
    print("deposit")
else:
    print("exit")


units=int(input("enter the units: "))
if units>=500:
    print("very high usage")

elif units>=300:
    print("high usage")
elif units>=100:
    print("medium usage")
else:
    print("low usage")


food_rating=int(input("enter the food rating: "))
if food_rating>=5:
    print("excellent")
elif food_rating>=4:
    print("good")
elif food_rating>=3:
    print("average")
elif food_rating>=2:
    print("poor")
else:
    print("very poor")


pin=78912
account_balance=7000
withdarwal_amount=5000
if pin==78912:
    if account_balance>=withdarwal_amount:
        print("withdrawal successful")
    else:
        print("insufficient balance")
else:
    print("invalid pin")

