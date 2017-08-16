"""Class Programing """
print("""__init__ has beeen overriding """)
class Baseclass(object):
    print ("Hi am from Baseclass")
    def __init__(self):
        print ("Hi am from Baseclass __init__")
        

class Dirclass(Baseclass):
    print ("Hi am form Dirclass of bass class")
    def __init__(self):
        print ("Hi am from Dircass __init__")

obj=Dirclass()

print("\n")
print("""___init__not been overridding use Superclass""")
class Baseclass(object):
    """ this doc about the class"""
    print ("Hi am from Baseclass")
    def __init__(self):
        print ("Hi am from Baseclass __init__")
        

class Dirclass(Baseclass):
    print ("Hi am form Dirclass of bass class")
    def __init__(self):
	    Baseclass.__init__(self)
	    print ("Hi am from Dircass __init__")

obj=Dirclass()
#print (dir(Dirclass))
Dirclass.__repr__
Dirclass.__doc__
print("\n")
#raw_input()
