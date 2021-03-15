import sys
import os
filename="samples/sample5.cpp"

code=[]

s= open(filename)

code =s.read()
def codeVonFilename(name:str):
    filename=os.getcwd()+"/PyPrgs/b03/samples/"+name+".cpp"
    with open(filename) as file:
        return file.read()

def checkblock(content:str):

    XC=content.splitlines()
    content=""
    acc_lines_len=[]
    acc=0
    for x in XC:# rechnen wie viel Char in jede Ziel 
        acc=acc+len(x)+1
        acc_lines_len.append(acc)
        content=content+(x.split("//")[0])+"\n"
        #entfernen alls nach "//"
    "check die Klammern und gebt uns  Tupel (zeile, spalte, msg)"
    
    i=0
    l1=[]
    l2=[]
    Klammern='"{}()[]]'
    while i<len(content):#l1 und l2 sind die Klammern und ihre bestemmt Position
        if content[i] in Klammern:
            l1.append(i)
            l2.append(content[i])
        i=i+1
    i=0
    l3=[]
    l4=[]
    kwatch=False
    while i< len(l1):# entfernen alles zwischen ""
        if l2[i]=='"':
            kwatch=not kwatch
            i=i+1
            continue
        if not kwatch:
            l3.append(l1[i])
            l4.append(l2[i])

        i=i+1
        if kwatch:
            print("error")
    K={"{":"}","[":"]","(":")"}

    #l4 in shape of ['(', ')', '{', ')']
    
    def T(start,end):
        if start-end==0:
            return None
      
        #search for the next
        try:
            key=l4[start]
            ind=l4[start:end].index(K[key])+start
        except:
            print("error")
            return start
        start=start+1
        return T(start,ind ) or T(ind+1,end)
        #verteilen jedes Satz und schaoen 
        # ob etwas falsch in jene gibt



    result=T(0,len(l4))

    if result==None:
        return (None, None ,None)
    else:
        n=l3[result]
        c=l4[result]
        m=None
        if c in ["{","[","("]:
            m="Klammer ist nicht geschlossen"
        else:
            m="extra Klammer"

        N=None
        i =0
        while i<len(acc_lines_len):
            if n<acc_lines_len[i]:
                N=i
                break
            i=i+1
        return (N,c,m)
    
    

print(checkblock(code))








    

