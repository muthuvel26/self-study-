import threading
import time
import os

def somemethod(num):
    """thread somemethod function"""
    print os.getpid()
    lock.acquire()
    print 'starting something' , str(num)
    time.sleep(3)
    print 'finishing something' , str(num)
    lock.release()
    return


lock = threading.Lock()


for i in range(5):
    t = threading.Thread(target=somemethod, args=(i,))
    t.start()
    

#somemethod(1)
#somemethod(2)
#somemethod(3)
#somemethod(4)
#somemethod(5)
""" done by sasken"""
