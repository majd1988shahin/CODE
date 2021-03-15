import os, sys
import PIL
from PIL import Image
import time

def PY(iname,oname,n):
    a=time.time()
    im =Image.open(iname)
    x,y=im.size
    for i in range(x):
        for j in range(y):
            r,g,b=im.getpixel((i,j))
            if r+g+b <n*3:
                im.putpixel((i,j),(0,0,0))
            else:
                im.putpixel((i,j),(255,255,255))
    im.save(oname)
    b=time.time()
    print("Es daurt  {0} Sekonde mit PY Funktion".format(b-a))

def EPY(iname,oname,n):
    a=time.time()
    im =Image.open(iname)
    x,y=im.size

    data=im.tobytes()
    print(type(data))
    odata = bytearray([0,0,0])*x*y

    #print(len(data),x*y*3)
    N=n*3# zum Zeitsparen in der inner Schleife
    for j in range(y):
        rawpos=j*x*3# zum Zeitsparen in der inner Schleife
        grawpos=j*x
        for i in range(x):
            pos=rawpos+i*3
            r,g,b=data[pos],data[pos+1],data[pos+2]
            if r+g+b >=N:
                odata[i+grawpos]=255
    oim=Image.frombytes("L",(x,y),bytes(odata))
    oim.save(oname)
    b=time.time()
    print("Es daurt  {0} Sekonde mit EPY Funktion".format(b-a))

def BPY(iname,oname,n):
    a=time.time()
    im =Image.open(iname)
    x,y=im.size
    oim=Image.new("L",size=(x,y))
    data=im.load()
    odata=oim.load()
    N=n*3
    for j in range(y):
        for i in range(x):
            if sum(data[i,j])>N :
                odata[i,j]=255
    
    oim.save(oname)  
    b=time.time()
    print("Es daurt  {0} Sekonde mit BPY Funktion".format(b-a))

import ctypes,os
import os
"""
def get_cFunk(): 
    path = os.path.join(os.getcwd(), "maxsub_c.so")
    clib = ctypes.cdll.LoadLibrary(path)
    c_int_p = ctypes.POINTER(ctypes.c_int)
    c_int = ctypes.c_int # shorter
    argtypes = [c_int_p, c_int, c_int_p, c_int_p]
    clib.maxsub_c.argtypes = argtypes
    return clib.maxsub_c


def maxsubc(lis):
    n=len(lis)
    arr=(ctypes.c_int*n)(*lis)
    start, end =ctypes.c_int(0),ctypes.c_int(-1)
    cf=get_cmaxsub()
    max_sum=cf(arr,n,ctypes.byref(start),ctypes.byref(end))
    return max_sum,start.value,end.value
    """

def CPY(iname,oname,n):

    a=time.time()
    im =Image.open(iname)
    x,y=im.size

    libc=ctypes.cdll.LoadLibrary("libc.so.6")
    path=os.path.join(os.getcwd(),"c_filter.so")
    clib=ctypes.cdll.LoadLibrary(path)
    c_P_data=ctypes.POINTER(ctypes.c_ubyte)
    c_int_size,c_int_th=ctypes.c_int,ctypes.c_int
    clib.c_filter.argtypes=[c_P_data,c_int_size,c_int_th]
    
    #clib.c_filter.restype=ctypes.POINTER(ctypes.c_ubyte) 
    outType=ctypes.POINTER( ctypes.c_ubyte)
    clib.c_filter.restype=outType
    data=im.tobytes()
    b=time.time()
    print(b-a)
    arr=(ctypes.c_ubyte * len (data))(*data)
    size=ctypes.c_int(x*y)
    deep=ctypes.c_int(3)
    th=ctypes.c_int(127)
    b=time.time()
    print(b-a)
    odata= clib.c_filter(arr,size,th) 
    #print(*odata)
    ss=odata[0]
    sd=odata[x*y+6]
    print(ss,sd,ctypes.sizeof(odata))
    b=time.time()
    print(b-a)
    odata2=bytes([odata[i] for i in range(x*y)])
    

    #odata2=bytes(*odata,x*y)
    oim=Image.frombytes("L",size=(x,y),data=odata2)
    oim.save(oname)
    b=time.time()
    print(b-a)


    
    
    


    
def main(args):
    if len(args)==1:
        iname,oname,k,n="ite.png","out_CPY.png","CPY",127
    elif len(args)==7:
        iname,oname,k,n=args[1],args[2],args[4],int(args[6])
    else :
        iname,oname,k,n=args[1],args[2],args[4],127
    
    if k=="PY":PY(iname,oname,n)#4.778 Sec
    elif k=="EPY":EPY(iname,oname,n)#0.7 Sec
    elif k=="BPY":BPY(iname,oname,n)#0.689
    else:
        CPY(iname,oname,n)#1.4386694431304932  :(



if __name__ == "__main__":
    main(sys.argv)