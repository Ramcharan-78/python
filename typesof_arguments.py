#positional arguments
"""def employee(name,age):
    print("name",name)
    print("age",age)
employee("veda",14)


#keyword arguments
def sum(n,v,r):
    print(n+v+r)

sum(v=7,n=8,r=1)

#default arguments
def game(name,mess):
    print(name,mess)
game(mess="hello",name="nani")"""


a=int(input("x"))
rev=0
if a<0:
    sign=-1
else:
    sign=+1
x=abs(a)
while x>0:
    y=x%10
    rev=rev*10+y
    x=x//10
print(rev)

