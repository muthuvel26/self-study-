import threading
import time

a = 100
                   
def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    time.sleep(2)
#    print a
#    print 'wait_for_event starting'
    event_is_set = e.wait()
#    print 'event is set . Now I am doing something'
    print a
    print 'done'

   
def do_somejob_event(e):
#    print 'doing some job'
    time.sleep(5)
    global a
    a = 300
#    print a
    e.set()

e = threading.Event()

t1 = threading.Thread( target=wait_for_event,
                      args=(e,))
t1.start()

t2 = threading.Thread( 
                      target=do_somejob_event,
                      args=(e,))
t2.start()