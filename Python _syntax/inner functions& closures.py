def Muthu():
    """ Method deceleration can be defiend in way of method itself  here method Muthu is defiend with arun method """
    a=100
    def arun():
        return 10+a
    return arun

obj=Muthu()
print(obj())

"""inner function is simply called as class function the below function is done with class as same as inner function """
class Muthu(object):
    def __init__(self,a=100):
        self.a=a
    def arun(self):
        return 10+self.a
obj1=Muthu()
print(obj1.arun())
'''-------------------------------------------------------------------------------------------------------------------'''
def Muthu(a=100):
    """ Method deceleration can be defiend in way of method itself  here method Muthu is defiend with arun method """
    def arun():
        return 10+a
    return arun

obj=Muthu(a=10)
print(obj())

"""inner function is simply called as class function the below function is done with class as same as inner function """
class Muthu(object):
    def __init__(self,a=100):
        self.a=a
    def arun(self,b):
        return 10+b
obj1=Muthu()
print(obj1.arun(10))
'''-------------------------------------------------------------------------------------------------------------------'''
def Muthu(func):
    """ Method deceleration can be defiend in way of method itself  here method Muthu is defiend with arun method """
    a=100
    def arun():
        return (10+a and func())
    return arun
"""
@Muthu
def sayhi():
    return "**********"
print (sayhi())
#sayhi=Muthu(sayhi) is @Muthu
"""
def sayhi():
    return "**********"
obj=Muthu(sayhi)
print(obj())
"""Here we are created new function obj with help of @muthu and @sayhi function"""
'''-------------------------------------------------------------------------------------------------------------------'''
"""Closure"""
def bill(*kwargs):
    def wtax(x):
        return sum(kwargs)+ x*sum (kwargs)
    return wtax

newbill=bill(100,23,65,73)
print 'Total Amount :'+str (newbill(0))
print 'Total Tax Amount :' + str(newbill(.18)-newbill(0))
print 'Total Pay Amount :'+ str(newbill(.18))

'''-------------------------------------------------------------------------------------------------------------------'''
