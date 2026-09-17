a={1,2,7,8,9,12,1,2,}
print(a)  # remove duplicates automitically
# it doesnt support indexing
a.add(912)
print(a)
a.update([10,20])
print(a)
a.remove(10)
print(a)
a.discard(20)
print(a)
a.pop()
print(a)
a.clear()
print(a)


#  set mathmathetical operations methods  
a={1,2,3,4}
b={4,5,6,7}
print(a.union(b))
print(a|b)  # another method of union 
print(a.intersection(b))
print(a&b) # another method of intersection
print(a.difference(b))  # difference a without common elements
print(a-b)  # another method of differnece 
print(a.symmetric_difference(b)) # symmetric diiference meanns writting elements are not common
print(a^b)  # another method of symmetric difference
# set relationship methods
print(a.issubset(b))   # subset means b contains all a elements 
print(a.isdisjoint(b))  # disjoint both doesnt share any element
print(a.issuperset(b))  # a contains all elements of b or reverse of subset

