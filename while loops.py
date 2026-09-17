"""
i=10
while i<0:
    print(i)
    i=i-1


i=0
while i<50:
     if i%2==1:
          print(i)
     i=i+1"""


n=7789
while n>0:
    x=n%10
    print(x,end="," )
    n=n//10


n=7789
rev=0
while n>0:
     x=n%10
     rev=rev*10+x
     n=n//10
print(rev)
print("hello world")