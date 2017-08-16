"""Mulitype inhertance"""
class A(object):
    pass
    print ("Am A")
class B(A):
    print ("Am B")
class C(A):
    print ("Am C")
class D(C,B):
    print ("Am D")
print ("""there is no __mro__ function avaliable on Dir(D)""")
print(dir(D))
print("\n")
print("The oder of Class Object flow:")
print(D.__mro__)

input()