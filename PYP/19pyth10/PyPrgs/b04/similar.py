import sys,os
from soundex import soundex
from functools import reduce

def similar(word="hallo",filename="/usr/share/dict/words"):
    checkaskiiword=lambda word: reduce( lambda x,y:x and y,
                                    list(map(lambda x:ord(x)<128,word)))
    allasciiwords=list(filter(checkaskiiword, open(filename).read().split()))
    wontedsoundex=soundex(word)
    result=list(filter(lambda w: soundex(w)==wontedsoundex,allasciiwords))
    print(result)
    
    return result

def main(args):
    if len(args)==1:
        similar()
    elif len(args)==2:
        similar(args[1])
    else:
        similar(args[1],args[2])
    return



if __name__=='__main__':
    main(sys.argv)