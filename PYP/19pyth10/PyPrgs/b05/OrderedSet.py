class OrderedSet(set):
    def __init__(self,data):
        d=sorted(data)
        super().__init__(d)
    def add(self,e):
        try:
            n=len(e)
            ndata=sorted([ele for ele in e if ele not in self])
            data=list(self)
            pos=self._getPos(ndata[0])
            Rdata=data[0:pos]+ndata+data[pos:]
            return OrderedSet(tuple(Rdata))
        except:
            data=list(self)
            pos=self._getPos(e)
            data.insert(pos,e)
            return OrderedSet(tuple(data))

    def _getPos(self,e):
        data=list(self)
        for i in range(len(data)):
            if e<data[i]:
                return i
        
    def __eq__(self,other):
        if len(self)!=len(other): return False
        else:
            for i in self:
                if i not in other:
                    return False
        return True
    def _spicial_vergleiche(self,other):
        D1=sum([i**2 for i in self])
        D2=sum([i**2 for i in other])
        if D1>D2:return 1
        elif D1<D2: return -1
        else: return 0
    def __lt__(self,other):
        return self._spicial_vergleiche(other)==-1
    def __gt__(self,other):
        return self._spicial_vergleiche(other)==+1


s=OrderedSet((1,5,3,7,10))
print(len(s))

q=OrderedSet({1, 2,8, 4, 5, 7,12})
print(s<q)
