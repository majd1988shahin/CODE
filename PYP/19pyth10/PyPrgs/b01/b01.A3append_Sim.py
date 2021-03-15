#!/usr/bin/python3
# * coding : utf-8 *
import sys

lis=[1,2,3]
print("List :",lis)
nlis=[4,5]
a=lis
lis[len(lis):len(lis)+len(nlis)]=nlis #"original loesung ist lis[l=nlis]"
print("bleibeibt die Liste sie selbst ?",lis is a)
print("extended List : ",lis)

tup=(1,2,3)
print("\nTupel :",tup)
tup=tup+(4,5)
print("Neu Tupel :",tup)

tup=1,2,3
ntup=4,5
try:
    tup[len(tup):len(tup)+len(ntup)]=ntup
    print("Extended Tupel :",tup)
except:
    print("Can not Tupel extending")

str="Majd"
print("\nString :",str)
str=str+" Shahin"
print("Neu String :",str)

str="Majd"
nstr="Shahin"
try:
    str[len(str):len(str)+len(nstr)]=nstr
    print("Extended String :",str)
except:
    print("Can not String extending")