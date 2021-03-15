import sys,os
from soundex import soundex
from functools import reduce

def checksimilar(filename="/usr/share/dict/words"):
    checkaskiiword=lambda word: reduce( lambda x,y:x and y,
                                    list(map(lambda x:ord(x)<128,word)))
    allasciiwords=list(filter(checkaskiiword, open(filename).read().split()))

    A={}
    for i in range(0,len(allasciiwords)):
        sdx=soundex(allasciiwords[i])
        if sdx in A:
            #A[sdx].append(allasciiwords[i])
            A[sdx]=A[sdx]+1
        else:
            A[sdx]=1
    A_sorted=sorted(A.items(),key=lambda x: x[1],reverse=True)
   # print(A_sorted)
    print("Top 10:")
    for i in range(0,10):
        print(A_sorted[i][0],"klingt:",A_sorted[i][1],"mal !")
    
    return A_sorted

def main(args):
    if len(args)==1:
        checksimilar()
    else:
        checksimilar(args[1])


if __name__=='__main__':
    main(sys.argv)