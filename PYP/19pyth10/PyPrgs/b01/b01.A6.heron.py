#!/usr/bin/python3
# * coding : utf-8 *
import sys
def heron(x,eps=1e-6):
    a=(1+x)/2
    while abs(a**2-x)>eps:
        a=(a+x/a)/2
    return a

print(heron(10,1e-6))
