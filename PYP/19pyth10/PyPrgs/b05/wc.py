import sys,os
class wc:
    def __init__(self):
        print("wc init")
        

    de="de"
    en="en"
    lang=de
    W_de=["Die Datei","hat","\tZeilen","\tWörter","\tBuchtaben"]
    W_en=["The file","has","\tlines","\twords","\tletters"]
    words=W_de

    def set_lang(self,x):
        if x==self.de:
            self.lang=de
            self.words=W_de
        elif x==self.en:
            self.lang=self.en
            self.words=self.W_en
        else:
            print("Die Sprache ist nicht erkannt")

    def wc_show(self,fileName):
        
        f=open(fileName).read()
        Zielen=len(f.splitlines())
        woerter=len(f.split(" "))
        bochstaben=len(f)-Zielen-woerter

        print (self.words[0],fileName,self.words[1])
        print (Zielen,self.words[2])
        print (woerter,self.words[3])
        print(bochstaben,self.words[4])
        
        

