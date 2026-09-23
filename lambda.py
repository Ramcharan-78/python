add=lambda a:a+10
print(add(7)) 


mini=lambda a,b,c:min(a,b,c)
print(mini(7,8,9))

li=[1,2,3,4,5,6,7]
result=list(map(lambda a:a*9/5+32,li))
print(result)

lis=["nani","ramu","veda"]
x=list(map(lambda a:a.upper(),lis))
print(x)



lis1=[1,3,4,5,6,7,8,9,52,]
v=list(filter(lambda a:a%2==0,lis1))
print(v)

lis1=[1,3,4,5,6,7,8,9,52,]
v=list(filter(lambda a:a>50,lis1))
print(v)

lis1=[1,3,4,5,6,7,8,9,52,50,15,]
v=list(filter(lambda a:a%5==0,lis1))
print(v)


lis2=["nanu","deepak","vedasri","chowdary"]
n=list(filter(lambda a:len(a)>5,lis2))
print(n)