""""Error Creation:"""
class Myerror(Exception):
    pass

if 11%2==0:
    print ("even number")
else:
    raise Myerror("CAN'T do it")
