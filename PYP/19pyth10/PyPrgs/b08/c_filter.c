#include<stdio.h>
#include <stdlib.h>
typedef unsigned char byte;

//creat hallo.o
//gcc -c -Wall -Werror -fpic c_filter.c
//creat hallo.so
//gcc -shared -o c_filter.so c_filter.o

byte * c_filter(byte *a,int n, int th)
{
    byte *res;
    res = (byte*)malloc(n * sizeof(byte));
    int opos=0;
    int N=0;
    int j=0;
    int Th=th*3;
    int end=n*3;
    for (int i =0;i<end;i+=3)
    {
        N=0;
        for (j=0;j<3;j++) 
        {N+=a[i+j];}

        res[opos]= N>Th? 255:0;
        opos++;
    }
    return res;
}
void pl(byte *a,int n)
{
    for (int i =0;i<n;i++)
    {
        printf("%d\n",a[i]);
    }
}
int main()
{
    byte a[]={1 , 2 ,3,4,5,6,7,8,9};
    //pl(a,9);
    //int *res=thr(a,3,3,4);
    
    byte * res=c_filter(a,3,6);
    pl(res,3);
    printf("fertig");
    return 0;
}