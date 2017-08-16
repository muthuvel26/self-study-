import subprocess
import time
cmd = ["adb devices"]
list1=[]
l2=[]
for adb in cmd:
    p = subprocess.Popen(adb,stdout=subprocess.PIPE,shell="TRUE")
    list1.append(p.stdout.read().decode('utf-8'))
test=list1[0].split()
l2=(test)
i=len(l2)
if i>4:
  for i in range(len(l2)):
    if i > 3 and i% 2==0:
      print (l2[i])
else:
    print ("Error in Devices connectivity")

print("\nPress Enter Key to Exit..!!")


