def f(a,b,c=1):
    print(a,b,c)

def g(a,b,c,**d):
    print(a,b,c,d)
def h(a,b,c,*d,**e):
    print(a,b,c,d,e)
    
f(1, 2, 3), f(1), f(1, 2), f(1, 2, 3, 4)
#f(1) error b ist nicht eingeganen
#f(1,2,3,4) es gibt nur 3 argeuments
g(1, 2), g(1, 2, 3, 4), g(1, 2, 3, 4, bla="bla")
#g(1,2) error c nicht eingegaben
#g(1,2,3,4) error weil d ist ein dicktionary , es geht aber mit vier =4
#g(1,2,3,4,bla="bla") error weil gibt es kein parametr fuer 4
h(1, 2, 3, 4, 5, 6, c=7), h(1, 2, 3, 4, 5, 6, x=7)
#h(1, 2, 3, 4, 5, 6, c=7) c ist zwei mal eingegeben

