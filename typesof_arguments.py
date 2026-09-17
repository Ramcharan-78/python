#positional arguments
def employee(name,age):
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
game(mess="hello",name="nani")


