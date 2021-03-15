import sys
import os
import string
import random

def main(arg):
    filename="/usr/share/games/fortunes/fortunes"
    #print(arg)
    with open(filename) as file:
        f= file.read()
    forts=[]
    if len(arg)>=2:
        if arg[1]=="-m":
            teil=arg[2]
            #print(teil)
            for s in f.split("\n%\n"):
                if teil in s:
                    forts.append(s)
    else:
        for s in f.split("\n%\n"):
            forts.append(s)
    if forts:
        r=random.randint(0,len(forts))
        print(forts[r])
    else:
        print("Ihre fortunes sind leer")
    
    


if __name__ == '__main__':
    main(sys.argv)





