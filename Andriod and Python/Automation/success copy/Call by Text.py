def tap(x,y):
    import os
    cmd='adb shell input tap {} {}'.format(x,y)
    print cmd
    os.system(cmd)
    
def axis(v):
    import re
    match=re.search(r"(\d+).*?(\d+).*?(\d+).*?(\d+)",v)
    x1=int(match.group(1))
    y1=int(match.group(2))
    x2=int(match.group(3))
    y2=int(match.group(4))
    axis=str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2)
    x=(x1+x2)/2
    y=(y1+y2)/2
    print 'X1 Y1 X2 Y2 :', axis
    return (x,y)

def callbytext():
    import xml.etree.ElementTree as ET
    tree = ET.parse('gm1.xml')
    root = tree.getroot()
    tag='node'
    print 'My serach attrib:'
    attrib='text'
    var='{}'.format(tag)
    print 'var is :' +str(var)
    print 'Enter Text to find bounds:'
    input=raw_input()
    class Myerror(Exception):
        pass
    for var in root.iter(tag):
        e=var.get(attrib)
        print e
        if e ==input:
            print 'yes'
            v=var.get('bounds')
            break
        v=None
    if v==None:
        raise Myerror("invalid input")
    return (v)


v=callbytext()
#v=callbypackage()
#v=callbyid()
#v=callbydescrtipon()
#v=callbybutton_property()
x,y=axis(v)
tap(x,y)


