import os, sys
import PIL
from PIL import Image
def finde(name):
    im =Image.open(name)
    x,y=im.size
    yy=y/2
    lis=[]
    i=0
    Rx,Gx,Bx=None, None,None
    while True:
        R,G,B=im.getpixel((i,y/2))
        if  R!=G and G!=B:
            break
        if R!=Rx:
            lis.append(R)
            Rx=R
            print(i)
        i+=1
    res=""
    
    for i in lis:
        res=res+chr(i)
    print(res)
    
    
def write(massage, name):
    im =Image.open(name)
    x,y=im.size
    if len(massage)<28:
        for i in range(28-len(massage)):
            massage+=" "
    lis=[ord(i) for i in massage] 
       
    for i in range(len(lis)):
        for d in range(10):
            for s in range(y//2-5,y//2+5):
                im.putpixel((i*10+d,s),(lis[i],)*3)
    im.save(name)


def main(argv):
    if len(argv)==1:
        finde("ite.png")
        #write("Die Nachricht","ite.png")
    else :
        if argv[1]=="-r":
            finde(argv[2])
        if argv[1]=="-w":
            write(argv[2],argv[3])

if __name__ == "__main__":
    main(sys.argv)