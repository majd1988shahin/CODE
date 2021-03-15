import urllib.request
import urllib.parse , time


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

rand = read_random(1,20,True)
randmm = read_random(17, 42, debug=True); 
print(" rand=%d" % rand)
print("randmm=%d" % randmm) 
#############
PMA="https://pma.inftech.hs-mannheim.de"
PMASTORE=PMA+"/wsgi/store"
def store_get():
    resp=urllib.request.urlopen(PMASTORE)
    if not resp.status==200:
        return None
    return resp.read().decode("UTF-8")

def store_post(msg):
    data=msg.encode("UTF-8")

    req=urllib.request.Request(PMASTORE,data=data)
    req.add_header("Content-Type","text/plain")
    resp=urllib.request.urlopen(req)
    if not 200<=resp.status<=299:
        return None
    return resp.read().decode("UTF-8")

now = "Hello %d" % int(time.time()*1000) 
print("storing %s" % now) 
posted = store_post(now) 
if posted != now:
    print("something changed that fast?\n")
    print(" we posted: |%s|" % now)
    print(" we got : |%s|" % posted)
time.sleep(1.0) 
msg = store_get()
print("getting %s" % msg)

