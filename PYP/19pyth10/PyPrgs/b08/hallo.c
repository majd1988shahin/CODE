#include<stdio.h>
//creat hallo.o
//gcc -c -Wall -Werror -fpic hallo.c
//creat hallo.so
//gcc -shared -o hallo.so hallo.o
/*
#libc=ctypes.cdll.LoadLibrary("libc.so.6")
    path=os.path.join(os.getcwd(),"hallo.so")
    clib=ctypes.cdll.LoadLibrary(path)
    #print(clib)
    a=ctypes.c_int(5)
    
    print(clib.hallo(a))"""
    */
int hallo(int a)

{
    
    printf("\n\nHello World,\nWelcome to my first C program on Ubuntu Linux\n\n");
    return a*a;
}
