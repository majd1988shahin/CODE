#!/usr/bin/python3
# * coding : utf-8 *
import sys

def main(arg):
    "Hello"
    print("Claculator!")

    exec("print("+("".join(arg[1:])+")"))
    calc(float(arg[1]),arg[2],float(arg[3]))

def calc(v1, op, v2):
    print(v1,op,v2," = ")
    if op=="+":
        print(v1+v2)
    elif op=="-":
        print(v1-v2)
    elif op=="*":
        print(v1*v2)
    elif op=="/":   
        print(v1/v2)
    else :
        print(op, "is not defind")
    


if __name__ == '__main__':
    main(sys.argv[:])
