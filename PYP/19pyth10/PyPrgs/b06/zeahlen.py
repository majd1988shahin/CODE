import os,sys

def main(args):
   
    text=str.lower( args[1]).split()
    dic=dict()

    for w in text:
        if w in dic:
            dic[w]=dic[w]+1
        else:
            dic[w]=1

    res=sorted(dic.items(), key=lambda kv: (kv[1],ord(kv[0][0])),reverse=True)
    print(res)

if __name__ == "__main__":
    #main(sys.argv)
    main(['mÄ',"ein Text wird ein Beispiel des weggeworfen wird"])