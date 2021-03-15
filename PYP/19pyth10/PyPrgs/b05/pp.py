def isprim(x):
  return [i for i in range(2,1+x//2) if x%i==0]==[]


def prim():
  i=2
  while 1:
    if isprim(i):
      yield i
    i+=1

def pprim():
  i=2
  while 1:
    if isprim(i) and isprim(i+2):
        yield (i,i+2)
    i+=1

def run():

    import time
    t1=time.time()
    x1=[i for i in range(2,1000) if isprim(i)]
    t2=time.time()
    print(t2-t1)

    P=prim()
    t1=time.time()
    x2=[next(P) for _ in range(len(x1))]
    t2=time.time()
    print(t2-t1)
    print (x1)

    PP=pprim()
    from itertools import islice
    print("Prim Paare:")
    print(list(islice(PP,0,100)))

#run()