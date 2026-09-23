
"""fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

num=(1,2,3,4,5)
for x in num:
  if x == 3:
    continue
  print(x)


for i in range(6):
   if i== 3:break
   print(i)
else: #if loops breaks , else block is not exists
   print("finaly completed")


num=("nani","deepu","fruits")
fruits=("apple","baanana","mango")
for y in num :
  for z in fruits:
    print(y,z)

n = 121
rev = 0
x=n

while n > 0:
    digit = n % 10        # take the last digit
    rev = rev * 10 + digit  # build the reversed number
    n = n // 10 
print(rev)
if rev==x:
    print("palindrme")
else:
    print("not palindrme")

fac=24
i=1
while i<=24:
    if fac%i==0:
        print(i,end=",")
    i=i+1



# Program to check if a number is perfect

num=int(input("entre your number"))
factors=0
for i in range(1,6):
     if num%i==0:
      factors=factors+i
if num==factors:
    print("perfect number")
else:
    print("not a perfect number")


let=1234
sum=0
while let>0:
    x=let%10
    sum=sum+x
    let=let//10
print(sum)


number=24
fac=0
for i in range(1,number+1):
    if number%i==0:
        fac=fac+1
if fac==2:
    print("prime num")
else:
    print("not a prime a num")


# nested loops
for i in range(0,1):
    for j in range(1,4):
       print(i,j)

# square pattern
row=5
for i in range(0,5):
    for j in range(0,5):
        print("*",end="")
    print(end="\n")


# right angle triangle pattern 
row=5
col=5
for i in range(0,5):
    for j in range(2*i-i):

        print("*",end="")
    print()

#reverse right angle triangle
row=6
col=6
for i in range(0,6):
    for j in range(6-i):
        print("*", end="")
    
    print()"""


# pyramid
row=5
col=5
rows = 5

"""for i in range(0,row):
    
    for j in range(row-i-1):
        print(" ", end="")
    
    for k in range(i+1):
        print("*", end=" ")
    print()


#reverse pyramid
for i in range(0,5):
    for j in range(i):
        print(" ",end="")
    for k in range(5-i):
        print("*",end=" ")
    print()



# number patterns square 
for i in range(1,6):
    for j in range(1,6):
        print(j,end="")
        
    print()


#right angle triangle number pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


# reverse right angle triangle pattern

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()"""



#floyd's triangle
n=5
a=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a+1,end="")
        a=a+1
    print()



