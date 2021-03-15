import urllib.request
import urllib.parse , time
import threading
from multiprocessing import Queue
class chat:
    def __init__(self,chatURL="https://pma.inftech.hs-mannheim.de/wsgi/chat"
                    ,end="!q",user="[sha]"):
        self.url=chatURL
        self.end=end
        self.user=user
        self.Queue=[]
        self.online=False
        self.tg=threading.Thread(target=self.run_get)
        self.ti=threading.Thread(target=self.run_input)

    def run_input(self):
        while self.online:
            s=input()
            if s==self.end:
                self.online=False
                self.callback()
                break
            self.post(s)
            time.sleep(0.1)
    def go_online(self,endstatment):
        self.callback=endstatment
        self.online=True
        self.post("is online")
        self.tg.start()
        self.ti.start()
    def go_offline(self):
        self.online=False
        self.post(" is offline")
        self.tg.join()
        self.ti.join()
    def run_get(self):
        while self.online:
            s=self.get().splitlines()
            s.reverse()
            for ss in s :
                if ss not in self.Queue:
                    self.Queue.append(ss)
                    print(ss)
                    
            time.sleep(0.3)
                

    def get(self):
        resp=urllib.request.urlopen(self.url)
        #print(resp.status)
        if not resp.status==200:
            return None
        result=resp.read().decode("UTF-8")
        return result


    def post(self,msg):

        data=(self.user+" : "+msg).encode("UTF-8")
        req=urllib.request.Request(self.url,data=data)
        req.add_header("Content-Type","text/plain")
        #print(req.data.decode("UTF-8"))
        resp=urllib.request.urlopen(req)
        if not 200<=resp.status<=299:
            return None
        return resp.read().decode("UTF-8")



def main(args):
    name="[sha]"
    if len(args)==2:
        name=args[1]
    c=chat(user=name)
    c.go_online(endstatment=lambda:c.go_offline)

import sys
if __name__=="__main__":
    main(sys.argv)