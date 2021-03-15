import sys

def ggTr1(x,y):
    if x<y:
        return ggTr1(y,x)
    elif x%y!=0:
        return ggTr1(x%y,y)
    else:
        return y

    print(ggTr1(10,30))

print(ggTr1(20,30))
print(ggTr1(2,5))
print(ggTr1(8,6))
print(ggTr1(7,3))



def ggTr2(x,y):
    if x<y:
        return ggTr2(y,x)
    elif x>y:
        return ggTr2(x-y,y)
    else:
        return y

print(ggTr2(10,30))
print(ggTr2(20,30))
print(ggTr2(2,5))
print(ggTr2(8,6))
print(ggTr2(7,3))


def ggt(x,y):
    
    while x%y!=0:
        if x<y:
            (x,y)=(y,x)
        x=x%y
    return y

print(ggt(10,30))
print(ggt(20,30))
print(ggt(2,5))
print(ggt(8,6))
print(ggt(7,3))

a=[]
s= open("ggts.dat")
    
s=s.read().splitlines()
print(s[0])