import os, sys
class count:

    f=""
    def __init__(self,filename):
        print("init count")
        self.f=open(filename).read()
        
    
    def count_words(self):
        words=[]
        counts=[]
        f="hallo hallo majd"
        allwords=self.f.split(" ")
        
        for w in allwords:
            if w in words:
                 ind =words.index(w)
                 counts[ind]=counts[ind]+1
            else:
                words.insert(-1,w)
                counts.insert(-1,1)
        R=dict(zip(counts,words))
        counts.sort()
        result=dict()
        for i in counts:
            result[i]=R[i]
        return result    


    