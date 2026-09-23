"""def help(i):
    if i==6:
        return
    else:
        print(i)
        help(i+1)
help(1)



def name(i,n):
    if i>n:
        return 
    else:
        print(i)
        name(i+1,n)
name(1,5)

def rev(n):
    if n==0:
        return 
    else:
        print(n)
        rev(n-1)

rev(5)"""


#factorial
def fac(n):
    if n==0 or n==1:
        return 1
    return n*fac(n-1)


print(fac(5))

# fibonaci sequence 
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
 
for i in range(10):
    print(fib(i),end=",")