""" Lambda is deceleration of the method with out body or single line """ 
print "enter a number to check even or not :" 
d=lambda x:x%2==0
print d(input())

"""
b=[]
for a in range(3):
    b.append(input())
print b
"""
print "enter size of list :"
x=input()
y=input()
print ("create a list of number ")
"""a=[a for a in range(x)]
print a"""
e=map(lambda a :a,range(x))
print e
print ("create a list of number with user input ")
e=map(lambda i:input(),range(x))
print e
"""
Note:
map is used for function with list of number 
map function always save as list
loop can be give as lambda as while with range
"""
