import sys
S={'B':1,'F':1,'P':1,'V':1,
    'C':2,'G':2,'J':2,'K':2,'Q':2,'S':2,'X':2,'Z':2,
    'D':3,'T':3,'L':4,
    'M':5,'N':5,'R':6,
    'A':None,'E':None,'I':None,'O':None,'U':None,'W':None,'Y':None,'H':None
    
    }
def soundex(name=""):
    name=name.upper()
    s1=[S[x] for x in list(filter(lambda x: (65<=ord(x)<=90 or (97<=ord(x)<=122))and S[x] ,list(name)[1:]))]+[0]
    s2=[ s1[i] for i in range(0,len(s1)-1) if s1[i]!=s1[i+1]]
    s3=s2+[0,0,0,0,0]
    
    return name[0]+"".join(map(str,s3[0:5]))


def main(argv):
    if len(argv)==1:
        argv=argv+["soundex","soundeggs","flurbel"]#"soundex","soundeggs",
    for name in argv[1:]:
        print(name," : ",soundex(name))

if __name__=='__main__':
    main(sys.argv)