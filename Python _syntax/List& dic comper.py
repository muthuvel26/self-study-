""" List compersion  and dictonary comperhension"""
x=[x for x in range(10)]
print(x)
type(x)
x=[x for x in range(10) if x%2==0]
print(x)
type(x)
list=[1,3,5,7,9]
x=[x for x in list if x%2==0]
print(x)
type(x)
x=[(x,y) for x in range(5)for y in range(5) if x%2!=0 and y%2!=0]
print(x)
type(x)
i=[(x,y,z)for x in range(5)for y in range(5)for z in range(5) if x%2!=0 and y%2!=0 and z%2==0]
print(i)
type(i)
