#data typpes
"""
   lists are used to store multiple items in a single variable
   
list=["apple", "banana", "cherry"]
print(list)
#list items re indexed ,the first iteam has index 0
#list can be changeable ,meaning is we can add amd remove,
#sice list is duplicative lists can have iteams with same value
list2=["apple", "bannana", "apple"]
print(list2)
print(len(list2))  #tells how many items are there in list
#list contains diff type of data types
list1=["nani", "nani", 34, True]
print(list1)
print(type(list1))
print(list1[2]) #gives the iteam AT 2 INDEX
print(list2[-1]) #-1 refers to last iteam,-2refer to last second iteam 

list4=["apple", "banna", "cherry", "orange", "red"]
print(list4[2:5]) #these gives the output the items for 2 to 5
print(list2[-2:-5])

#to determine if a specfic element is present in list or not
list5=["apple", "banana", "nani"]
if "apple" in list5:
   print("yes,apple is present")
else:
      print("no apple is not present")  

#we want to change a specific value in list
thislist=["apple", "banana","cherry"]
thislist[1]="blackcurrent"
print(thislist)

#change range of iteams 
# we add emojis in the list 
emoji=["❤️","🤞","🥱"]
print(emoji)
cars=["bmw","mercides","landrover","suziki"]
print(cars)
cars.pop(1)  # we pop where we have to use only index  and we remove to use what we have to remove
print(cars)  
cars.remove("suziki")
fruits=["bananan", "mango","apple"]
cars.extend(fruits)  #extend to extend the list by adding another list 
print(cars)

#we use insert  to insert a element at specific index
cars.index("rangerover")
print(cars)

# list in idexing and slicing  we  use list method we kept list because list can store more values
print(list(2,10,1))
print(list(1,20,4)) # we use tuple or set inplace list 


numbers_nani=[10,20,30,40,50]
print(numbers_nani[-5:-1])
print(numbers_nani[-5:-1:2])
print(numbers_nani[::1])
print(numbers_nani[::2])
print(numbers_nani[::-1])
print(numbers_nani[::-2])
print(numbers_nani[:4:1])
print(numbers_nani[:5:1])

#nested list
v=[
    [0,10,20],
    [20,30,40],
    [7,8,9,12]
]
print(v)
print(v[0][1])
v.append([9,8,912])
print(v)"""

a=[1,2,3,4,7,8,9,12]
b=sorted(a)   # sorted is used to created a new list
print(a)
print(b)


