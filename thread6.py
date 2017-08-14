import threading
import time

a =45600

def somemethod(num, lock):
    """thread somemethod function"""
       
    global a
    lock.acquire()
    c = a
    time.sleep(1)
    c = c + 1
    a = c
    print a
    lock.release()
    
    return

threads = []
lock = threading.Lock()

for i in range(5):
    t = threading.Thread(name = 'myname' + str(i),  target=somemethod, args=(i,lock))
    t.start()