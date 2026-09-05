def days(x):
    match x:
        case 1:
            print("monday")
        case 2:
            print("tuesday")
        case 3:
            print("wednesday")
        case 4:
            print("thursday")
        case 5:
            print("friday")
        case 6:
            print("saturday")
        case 7:
            print("sunday")
        case _:
            print("invalid")


days(2)
days(10)
days(7)


def num_check(x):
    match x:
        case n if n>0:
            print("positive num")
        case n if n==0:
            print("zero")
        case n if n<0:
            print("negative num")

num_check(1)
num_check(0)


def atm(data):
    match data:
        case 1:
            print("check balance: 10000")
        case 2:
            print("withdaraw ")
        case 3:
            print("deposit")
        case 4:
            print("exit")

atm(1)


def food(data):
    match data:
        case 1:
            print("pizza")
        case 2:
            print("burger")
        case 3:
            print("biryani")
        case 4:
            print("dosa")
        case _:
            print("not avaliable")
food(4)
food(10)

