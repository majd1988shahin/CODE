class mange(set):
    
    def __init__(self):
        self.data=[]
        super().__init__()
        

    def add(self,e):
        if e not in self.data:
            self.data.insert(-1,e)
        else:
            print(e,"ist schon da")
    
    def union_update(self,seq):
        for e in seq:
            self.add(e)

    @staticmethod
    def union(seq):
        m=mange()
        m.union_update(seq)
        return m
    
    def remove(self,e):
        if e in self.data:
            self.data.remove(e)
        else:
            print(e," ist nicht da zum Loeschen")
    def difference_update(self,seq):
        for e in seq:
            self.remove(e)
    
    def difference(self,seq):
        d=list(filter(lambda e: e not in seq,self.data))
        return mange.union(d) 
        
    def clear(self):
        del self.data
        self.data=[]

    def size(self):
        return len(self.data)

    def __contains__(self,e):
        return e in self.data
    #def __iter__(self):
    #    return iter(self.data)
    def __iter__(self):
        self.idx=0
        return iter(self.data)

    def __next__(self):#nicht wichtig !!?
        if self.idx>len(self.data):
            raise StopIteration
        self.idx+=1
        return self.data[self.idx-1]

    def __eq__(self,other)->bool:

        if len(self.data)!=len(other.data):
            return False
        for e in self:
            if e not in other:
                return False

        return True
    def __ne__(self,other):
        return not self==other

    def __repr__(self):
        return self.data.__repr__()

    def __add__(self,e):
        try:
            self.union_update(e)
        except:
            self.add(e)
        
        return self
    def __sub__(self,e):
        try:
            self.difference_update(e)
        except:
            self.remove(e)
        return self
a=[1,2,3,4,2]
m=mange.union(a)
n=mange.union([3,2,1,5])

m=m+[5,8,9]
m=m+10
m= m-n
for i in m :
    print(i)

