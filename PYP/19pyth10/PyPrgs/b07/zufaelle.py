import timeit

import urllib.request, threading
import urllib.parse , time,timeit,random


BASE_URL = "https://pma.inftech.hs-mannheim.de"

def read_random(min=None,max=None,debug=False):
    randurl=BASE_URL+"/wsgi/rand"
    dic={}
    if max is not None: dic["max"]=max
    if min is not None: dic["min"]=min
    if dic:
        randurl+="?"+urllib.parse.urlencode(dic)
    if debug:
        print(randurl)
        print(urllib.parse.urlencode(dic))
    response= urllib.request.urlopen(randurl)
    return int(response.read())



t1=time.time()
while True:
    rand = read_random(1,100,False)
    print(" rand=%d" % rand)
    if (rand==17) or (rand==42):
        print("fertig")
        break
t2=time.time()
print("Es dauert: %d ms"%((t2-t1)*1000))

####mit threading
isfound=False

def read_random2(min=None,max=None,debug=False):
    global isfound
    while not isfound:
        randurl=BASE_URL+"/wsgi/rand"
        dic={}
        if max is not None: dic["max"]=max
        if min is not None: dic["min"]=min
        if dic:
            randurl+="?"+urllib.parse.urlencode(dic)
        if debug:
            print(randurl)
            print(urllib.parse.urlencode(dic))
        response= urllib.request.urlopen(randurl)
        res=None
        if not isfound:
            res=int(response.read())
            print("rand=",res)
        if res==17 or res == 42:
            print("isfound")
            isfound=True
            t2=time.time()
            print("Mit threading dauert es :",(t2-t1)*1000,"ms")


def th(n=17,min=0,max=100,debug=False):
    thn=[]
    param={min,max,debug}
    for i in range(n):
        t=threading.Thread(target=read_random2,args=param)
        thn.append(t)
    for t in thn:
        t.start()
    for t in thn:
        t.join()

print("serching mit 17 thread !")
t1=time.time()
th()
#je mehr threads desto schneller Ergebmnis bekommen !


    