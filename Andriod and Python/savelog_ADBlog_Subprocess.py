import subprocess
import time

testset=["radio","main","events"]
def savelog():
    s=time.clock()
    for i in testset:
        x="adb logcat -b {} -v time>{}_log.txt".format(i,i)
        print('**** %s logcat Execution Started**** \n'%i)
        subprocess.call(x ,shell=True)
    e=time.clock()
    print('TOTTAL TIME:',e-s)


savelog()
