import sys

def main(args):
    fileName=args[1]
    print(objread(fileName))

def objread(fileName,t="int"):
    punkte=[]
    dreiecke=[]
    try:
        with open(fileName) as f:
            F=f.readlines()
            for z in F:
                zeil=z.split()
                if len(zeil)>=4 :
                    if z[0]=='v':
                        if(t!="int"):
                            punkte.append((float(zeil[1]),float(zeil[2]),float(zeil[3])))
                        else:
                            punkte.append((int(zeil[1]),int(zeil[2]),int(zeil[3])))
                    if z[0]=="f":
                        dreiecke.append((int(zeil[1]),int(zeil[2]),int(zeil[3])))
    except :
        print(fileName,"read Error !")
        return 
    return (punkte,dreiecke)
    

if __name__ == "__main__":
    if len(sys.argv)>=2:
        main(sys.argv)
    else:
        main(['s',"simple.obj"])

