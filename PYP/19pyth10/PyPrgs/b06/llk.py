import sys

def main(args):
    text=filter (lambda c: str.isalpha(c),str.lower( args[1]).split())
    
    result=''
    for w in text:
        temp=None
        n=0
        nw=[]
        for c in w:
            if temp!=c:
                temp=c
                if n>1: 
                    nw.append(n.__repr__())
                n=1
                nw.append(c)
            else:
               n+=1
        if n>1: 
            nw.append(n.__repr__())
        
        result=result+"".join(nw)
        result=result+" "
    
    
    print(result)


if __name__ == "__main__":
    #main(sys.argv)
    main(['s','aaaaabbb dddddddddddxxxx ssdfdfgfgdd'])