import threading
import time

def somemethod(num):
    """thread somemethod function"""
    print threading.currentThread().getName(), 'Starting'
    if threading.currentThread().getName() == 'MainThread':
        print "I print this only for the main thread********"
    time.sleep(3)
    print threading.currentThread().getName(), 'Finishing'
    return

somemethod(100)
    
for i in range(5):
    t = threading.Thread(name = 'myname' + str(i),  target=somemethod, args=(i,))
    t.start()