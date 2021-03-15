#!/usr/bin/python3
# * coding : utf-8 *
import sys

lis=[1,2]
lis.append(lis)
print(lis)
print(lis[2])
print(lis[2][2])
print(lis[2][2][2])
#lis hat in Postion 2 ein Link/Pointer nach lis selbest

lis=[1,2]
lis=lis+lis;print(lis)