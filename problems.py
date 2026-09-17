#sum of digits in numbers is divisible by number 
"""num=int(input("entre a number:"))    
sum=0
v=num
while num>0:
    x=num%10
    sum=sum+x
    num=num//10

print(sum)

if v%sum ==0:
    print("harshad number")
else:
    print("not a harshad number")
# hackerrank problem
n = int(input("Enter an integer: "))
# hacker lank problem
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")"""



num1=int(input("entre your num"))
a=0
b=1

for i in range(num1):
    result=a+b
    print(a, end=",")
    a=b
    b=result
  
    


