import subprocess
import threading
import time

def devicesinfo():
    obj=subprocess.check_output('adb devices',shell=True,stderr=subprocess.STDOUT)
def savelog(i):
    x="adb logcat -b {} -v time>{}_log.txt".format(i,i)
    print('**** %s logcat Execution Started****\n'%i)
    subprocess.call(x ,shell=True)   
def viewlog(i):
    x="start adb logcat -b {} -v time".format(i)
    subprocess.call(x ,shell=True)
def start():
    devicesinfo()
    testset=["main","events","radio"]
    for i in testset:
        t1 = threading.Thread(target=savelog, args=(i,))
        t1.start()
        t2 = threading.Thread(target=viewlog, args=(i,))
        t2.start()
start()
print("TO Save logfile and exit kindly press key [y]")
print(sys.argc[0])
while True:
    a =input()
    if a == 'Y' or a == 'y':
        subprocess.call('adb kill-server' ,shell=True)
        break
    else:
        print("*****Kindly press 'y' to savelogfile*******")
        continue
    
