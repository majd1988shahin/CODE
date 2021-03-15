import time

def smartPrim():
    prims=[2]
    i=3
    while 1:
        if [x for x in prims if x<1+i//2 and i%x==0 ]==[]:
            yield i
            prims.append(i)
        i+=1    




ep=smartPrim()
print("smartPrim")
t1=time.time()
x3=[2]+[next(ep) for _ in range(1000)]
print(x3[-1])

t2=time.time()
print(t2-t1)  