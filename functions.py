"""def games(x):
    print(f"{x} is a game")
games(("free fire"))
games("bgmi")

def printonetoten():
    for i in range(10):
        print(i,end=",")

printonetoten() 
print()
printonetoten()
print()
printonetoten()
 


def sum(a,b):
    print(a+b)
def multi(a,b):
    print(a*b)
def division(a,b):
    print(a/b)
sum(7,8)
multi(7,12)
division(12,8)

def rec(a,b):
    print(a*b)
rec(9,12)


def add(a,b):
    return a+b
result=add(3,4)
print(result)



def maxium(a,b):
     return max(a,b)
print(maxium(10,15))

def voting(age):
     if age>=18:
         return True
     else:
          return False
print(voting(18))


def sum_num(N):
     sum=1
     for i in range(N):
          
          sum=sum+i
     return sum
print(sum_num(5))


def reverse(x):
     return str(x)[::-1]
print(reverse(1214))

def palindrome(x):
     return str(x)==str(x)[::-1]

def total(p,q):
     x=p*q
     
     return x

x=total(100,5)
y=x*0.1
print(x-y)  


def total_marks(m1,m2,m3):
    return m1+m2+m3
x=total_marks(90,90,90)
y=x/3
print(y)


# global +local variable
a=10
def helf():
    a=20
    print(a)
helf()
print(a)"""



n=int(input())
sum=0
while n>0:
    last=n%10
    sum=(sum*2)+last*2
    n=n//10
    last2=sum%10
    a=last2
    if a==1:
        print("true")
        break
else:
    print("false")
     
       
 

     
          