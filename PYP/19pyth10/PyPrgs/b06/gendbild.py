
def objread(fileName):
    punkte=[]
    dreiecke=[]
    try:
        with open(fileName) as f:
            F=f.readlines()
            for z in F:
                zeil=z.split()
                if len(zeil)>=4 :
                    if z[0]=='v':
                        punkte.append((int(zeil[1]),int(zeil[2]),int(zeil[3])))
                    if z[0]=="f":
                        dreiecke.append((int(zeil[1]),int(zeil[2]),int(zeil[3])))
    except :
        print(fileName,"read Error !")
        return 
    return (punkte,dreiecke)

(punkte,dreiecke)=objread("simple2.obj")
print(punkte)
print(dreiecke)
from genpbild import genpbild
genpbild("simple2.obj")