import subprocess
import time
cmd = ["adb devices"]
list1=[]
list2=[]
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
      s1="adb -s "
      s2= [" shell getprop ro.product.model"," shell getprop ro.build.id"," shell getprop ro.build.version.release"," get-serialno" ]
      for j in range(4):
          c='{}{}{}'.format(s1,l2[i],s2[j])
          print(c)
          p = subprocess.Popen(c,stdout=subprocess.PIPE,shell="False")
          list2.append(p.stdout.read())
  for i in range(len(list2)):
      print("Devices Details: " + list2[i].decode("utf-8"))
else:
    print ("Error in Devices connectivity")

print("\nPress Enter Key to Exit..!!")


