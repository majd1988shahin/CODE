import sys,re
##mit Hilfe von https://regex101.com/

def get_text(fileName):
    with open(fileName,"r") as f:
        res=f.readlines()
    return res
def get_Postzahl(text):
    postzahe_ausdruck=r"PLZ\s*\d\s*(\w*)"
    print("\nserching for postzahe_ausdruck mit ausdruck :",postzahe_ausdruck)
    res=[]
    for line in text:
        PLZ=re.search(postzahe_ausdruck,line)
        if PLZ is not None:
            print(PLZ[1])
            res.append(PLZ[1])
def get_Datum(text):
    DatumAusdruck=r"[\w]*\s\d\s([0-9]+).([0-9]+).([0-9]{4})"
    print("\nserching for DatumAusdruck mit ausdruck :",DatumAusdruck)
    res=[]
    for line in text:
        Datum=re.search(DatumAusdruck,line)
        
        if Datum is not None:
            Tage,Monat,Jahr=Datum.group(1,2,3)
            print("Tage= {0} , Monat= {1} , Jahr= {2}".format(Tage,Monat,Jahr))
            res.append([(Tage,Monat,Jahr)])

def get_Euro_Betreage(text):
    Euro_Betreage=r"EUR\s\d\s(\d*,\d*|\d*\.\d*.\d*|\d*).*"
    print("\nserching for Euro_Betreage mit ausdruck :",Euro_Betreage)
    res=[]
    for line in text:
        Eur=re.search(Euro_Betreage,line)
        if Eur is not None:
            print(Eur[1])
            res.append(Eur[1])

def get_Tel(text):

    Telausdruck=r"Tel\s\d\s([\d+-/ ]*).*"
    print("\nserching for Telephonnummer mit ausdruck :",Telausdruck)
    res=[]
    for line in text:
        Tel=re.search(Telausdruck,line)
        if Tel is not None:
            print(Tel[1])
            res.append(Tel[1])
def get_E_mail(text):
    E_mailausdruck=r"Email\s\d\s([\w.-]*@.*)"
    print("\nserching for E-Mail mit ausdruck :",E_mailausdruck)
    res=[]
    for line in text:
        E_mail=re.search(E_mailausdruck,line)
        if E_mail is not None:
            print( E_mail[1])
            res.append(E_mail[1])
def main(text):
    
    get_Postzahl(text)
    get_Datum(text)
    get_Euro_Betreage(text)
    get_Tel(text)
    get_E_mail(text)
        




if __name__=="__main__":
    fileName="reg.txt"
    if len (sys.argv)==2:
        fileName=sys.argv[1]
    text=get_text(fileName)
    main(text)