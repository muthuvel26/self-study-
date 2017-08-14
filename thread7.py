from multiprocessing import Pool
import os

def f(x):
    return str(x*x) + "from " + str(os.getpid())

if (__name__=='__main__'):
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))