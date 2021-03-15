#!/usr/bin/python3
# * coding : utf-8 *
import sys
import PIL.Image as Image


def main(arg):
    "imagmanip"

    if len(arg)!= 5:
        print("args muss : p inputfile outputfile")
        return
    op=arg[1]
    if op=="heller":
        heller(arg[2:])
    elif op=="gamma":
        gamma(arg[2:])
    elif op=="spreizen":
        spreizen(arg[2:])
    elif op=="binarisieren":
        binarisieren(arg[2:])
    else:
        print("Operation Error!")

def spreizen(args):
    
    [val,infile,outfile]=args
    V=255
    img=Image.open(infile)
    cols,rows=img.size
    
    print("in process : spreizen")
    p=float(val)
    if p < 0: 
        p=0
    if p>100:
        p=100
    a=V
    b=0

    x=0#finden Minimum und Maximum Werts im Bild
    while x<cols:
        y=0
        while y<rows:
            v=img.getpixel((x,y))
            if a>v:
                a=v
            if b<v:
                b=v
            y=y+1
        x=x+1
    print("minimum :",a,", maximum :",b)
    a=int(a*(100-p)/100)
    b=int(b+(V-b)*p/100)
    x=0
    while x<cols:
        y=0
        while y<rows:
            v=img.getpixel((x,y))
            v=int(V*(v-a)/(b-a))
            img.putpixel((x,y),v)
            y=y+1
        x=x+1
    img.save(outfile)
    print("done")
    return
def binarisieren(args):
    
    [val,infile,outfile]=args
    V=255
    img=Image.open(infile)
    cols,rows=img.size
    print("in process : binarisieren")
    s=int(val)
    if s < 0: 
        s=0
    if s>V:
        s=V

    x=0
    while x<cols:
        y=0
        while y<rows:
            v=img.getpixel((x,y))
            if v>=s:
                v=V
            else:
                v=0
            img.putpixel((x,y),v)
            y=y+1
        x=x+1
    img.save(outfile)
    print("done")
    return

def heller(args):

    [val,infile,outfile]=args
    V=255
    img=Image.open(infile)
    cols,rows=img.size
    print("in process : heller")
    p=int(val)
    if p < -100: 
        p=-100
    if p>100:
        p=100

    x=0
    while x<cols:
        y=0
        while y<rows:
            v=img.getpixel((x,y))
            v=int(v+V*p/100)
            if v>V : v=V
            if v<0 : v=0
            img.putpixel((x,y),v)
            y=y+1
        x=x+1
    img.save(outfile)
    print("done")
    return
def gamma(args):
    
    [val,infile,outfile]=args
    V=255
    img=Image.open(infile)
    cols,rows=img.size
    
    print("in process : gamma")
    gamma=float(val)
    if gamma < 0.0: 
        gamma=0.0
    if gamma>10.0:
        gamma=10.0
    x=0
    while x<cols:
        y=0
        while y<rows:
            v=img.getpixel((x,y))
            
            v=float(v)/V 
            v=255*((v)**gamma)
            v=int(v)
            if v>V : v=V
            if v<0 : v=0
            
            img.putpixel((x,y),v)
            y=y+1
        x=x+1
    img.save(outfile)
    print("done")
    return


if __name__ == '__main__':
    main(sys.argv[:])
