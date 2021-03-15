import sys,os


DE=["Die Datei","hat\n","Zeilen\n","Wörter\n","Buchstaben"]
EN=["The file","has\n","Lines\n","Words\n","Letters"]
sprache=DE
def set_lang(_sprache):
    if _sprache=="de":
        sprache=DE
    if _sprache=="en":
        sprache=EN

def wc_show(fileName):
    print(sprache[0],fileName,sprache[1],lins(fileName),sprache[2],
        words(fileName),sprache[3],chars(fileName),sprache[4])

def main(argv):
    fileName=argv[0]
    wc_show(fileName)


def chars(fileName):
    result=0
    result= [c for c in open(fileName).read() if str.isalpha(c)]
    return len(result)

def words(fileName):
    return len(open(fileName).read().split())

def lins(fileName):
    return len(open(fileName).readlines())

print("wc Module ist da!")
if __name__ == "__main__":
    #main(sys.argv)
    main(["wc.py"])