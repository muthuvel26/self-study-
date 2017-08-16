import threading
import time

a = 100
					
def wait_for_event(epub, econ):
	"""Wait for the event to be set before doing anything"""
	
	for i in range(5):
		epub.wait()
		print a
		epub.clear()
		econ.set()
   
def do_somejob_event(epub, econ):
	global a
	a = 300
	for i in range(5):
		a+=100	
		epub.set()
		econ.wait()
		econ.clear()
		
#	e.set()

epub = threading.Event()
econ = threading.Event()

t1 = threading.Thread( target=wait_for_event,
					  args=(epub,econ))
t1.start()

t2 = threading.Thread( 
					  target=do_somejob_event,
					  args=(epub,econ))
t2.start()