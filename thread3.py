import threading
import time

def somemethod(num):
    """thread somemethod function"""
    
    print threading.currentThread().getName(), 'Starting'
    
    time.sleep(3)
    if threading.currentThread().getName() == 'MainThread':
        print "only Main"
    print threading.currentThread().getName()+ 'Ending'
    return

    
print "From Main " + threading.currentThread().getName()
threads = []
for i in range(5):
    t = threading.Thread(name = 'myThread-' + str(i),  target=somemethod, args=(i,))
    
    threads.append(t)
    t.start()
    
somemethod(100)