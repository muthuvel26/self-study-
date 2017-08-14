import threading
import time

a = 100
                    
def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    time.sleep(2)
#    print 'wait_for_event starting'
    event_is_set = e.wait()
	print a
    event_2 = e2.wait()
#    print 'event set:', event_is_set
#    print 'event is set . Now I am doing something'
    print a
#    print 'done'

   
def do_somejob_event(e):

    print 'doing some job'
    time.sleep(5)
    global a
    a = 300
    e.set()
    e1.set()

def do_someother_event(e):

    print 'doing some job'
    time.sleep(1)
    e1.wait()
	time.sleep(4)
    global a
    a = a + 300
    e2.set()
    
e = threading.Event()
e1 = threading.Event()
e2 = threading.Event()


t1 = threading.Thread( target=wait_for_event,args=(e,))
t1.start()

t2 = threading.Thread( target=do_somejob_event,args=(e,))
t2.start()

t3 = threading.Thread( target=do_someother_event,args=(e,))
t3.start()