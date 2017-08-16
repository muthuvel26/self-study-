def sayhi():
    return "am return hi"
print(sayhi())

a=sayhi

def someotherhi(func):
    return func()
print (someotherhi(a))
    
