# IN tuple we cannot add or remove thr element once tuple is created
fruits=("apple", "banana", "cherry")
red, blue, yellow = fruits     # this is unpacking the tuple 
print(blue)
print(red)
print(yellow)
#extract the values into vaiables is called unpacking
animals=("cat", "dog", "rabbit","tiger", "lion")
(a,*b,c)=animals
print(a)
print(b)
print(c) 

# if we want to add a element in tuple we want to chagr it to list
tuple2=("nani","deepu","ram")
list1=list(tuple2)
list1.append("punith")
tuple1=tuple(list1)
print(tuple1)

if "nani" in tuple1:
    print("it is avaiable in tuple")
else:
    print("it is not avalible in tuple")

for i in range(len(tuple2)):
    print(tuple2[i])

while i>len(tuple1):
    print(tuple1[i])


# we can add two tuple into one tuple

tuple3=tuple1+tuple2
print(tuple3)

tuple4=tuple2*2 
print(tuple4) # means tuples  prints two times 6ye


# COUNT IS USEd to count how many elements present in a tuple 
tuple5=tuple2.count("nani")
print(tuple5)

a=(10,20,30)
print(a.index(20))

a=20
b=10
a,b=b,a
print(a)
print(b)


# another method
A=10
B=20
A=A+B
B=A-B
A=A-B
print(A)
print(B)