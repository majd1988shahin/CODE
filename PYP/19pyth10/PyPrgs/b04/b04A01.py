#!/usr/bin/python3

kubik=[]
kubik= [x**3 for x in range(1,10)]
print(kubik)

z=123456
alleTeiler=[x for x in range(2,1+z//2) if z%x==0 ]
print (alleTeiler)

prim=[y for y in range(10000,10100) if not [x for x in range(2,1+int(y**0.5)) if y%x==0]]

print (prim)

############
kubik=list(map(lambda x:x**3,list(range(1,10))))
print(kubik)

z=2*6*3*7*11
alleTeiler=list(filter(lambda x: z%x==0 and x<z,list(range(2,123456))))
print ("alle teiler ",z,"sind \n ",alleTeiler)

from functools import reduce

#Teiler=lambda x: list(filter(lambda i:x%i==0,list(range(2,x))))

#isprime=lambda x: list(filter(lambda i:x%i==0,list(range(2,x))))==[]
#allprim=list(filter(isprime,list(range(10000,10100))))

allprim=list(filter(lambda x: list(filter(lambda i:x%i==0,list(range(2,1+int(x**0.5)))))==[],
    list(range(10000,10100))))
print(allprim)