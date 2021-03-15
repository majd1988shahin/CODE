import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
from readobj import objread as objread
im =Image.new("1",(400,400))
[im.putpixel((i,j),0) for i in range(1,400) for j in range(1,400)]
for i in range(1,400):im.putpixel((i,i),1)
#im.show()
im.save("a1.png")

def machebild(punkte=[()], name="bild",mode="xy",deriecke=[()]):
    Max=0
    data=[]
    

    for p in punkte:
        n=(int(p[0]),int(p[1]),int(p[2]))
        Max=max(max(n),Max)
        data.append(n)
    Max+=1
    if deriecke!=[] and len(punkte)>=3:
        mode="all"
        imxy=Image.new("1",(Max,Max))
        imyz=Image.new("1",(Max,Max))
        imxz=Image.new("1",(Max,Max))
        drawxy=ImageDraw.Draw(imxy)
        drawyz=ImageDraw.Draw(imyz)
        drawxz=ImageDraw.Draw(imxz)
        for d in deriecke:
            P=[punkte[p-1] for p in d ]
            
            drawxy.polygon([(p[0],p[1]) for p in P],outline=128)
            drawyz.polygon([(p[1],p[2]) for p in P],outline=128)
            drawxz.polygon([(p[0],p[2]) for p in P],outline=128)
            imxy.save(name+"_xy.png")
            imyz.save(name+"_yz.png")
            imxz.save(name+"_xz.png")
        return
    if mode=="all":
        imxy=Image.new("1",(Max,Max))
        imyz=Image.new("1",(Max,Max))
        imxz=Image.new("1",(Max,Max))
        for p in data:
            imxy.putpixel((p[0],p[1]),1)
            imyz.putpixel((p[1],p[2]),1)
            imxz.putpixel((p[0],p[2]),1)
        imxy.save(name+"_xy.png")
        imyz.save(name+"_yz.png")
        imxz.save(name+"_xz.png")
        return
    
    fileName=name+"_"+mode+".png"
    im=Image.new("1",(Max,Max))
    if mode=="xy":
        for p in data:
            im.putpixel((p[0],p[1]),1)
    if mode=="xz":
        for p in data:
            im.putpixel((p[0],p[2]),1)
    if mode=="yz":
        for p in data:
            im.putpixel((p[1],p[2]),1)
    im.save(fileName)

def main(args):
    if len(args)==2:
        name=args[1].split('.')[0]
        print(name)
        genpbild(name)
    else:
        genpbild("simple2.obj")


def genpbild(name):
    (punkte,dreiecke)=objread(name,"int")
    print(punkte)
    machebild(punkte,name,"all",deriecke=dreiecke)
    

import sys
if __name__=="__main__":
    main(sys.argv)