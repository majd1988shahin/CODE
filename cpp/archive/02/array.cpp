#include <iostream>
#include <iomanip>
#include "funcs.h"

#define USE_NEW
#ifdef USE_NEW
#include <new>
#else
#include <cstdlib>
#endif

using namespace std;

double balance[5] = {1000.0, 2.0, 3.4, 17.0, 50.0};

Array creat_random_array(int size)
{
    Array a;
    a.size=size;
    #ifdef USE_NEW
        a.p=new (nothrow) int[size];
    #else
        a.p=(int*)malloc(size*sizeof(int));
    #endif
    if (a.p==NULL)
    {
        cout<<"can not allocate array \n";
        return a;
    }
    for (int i =0;i<size;i++)
        a.p[i]=random_(i);

    return a;
}

void print_array(Array a)
{
    if (a.p==NULL || a.size==0)
    {
        cout<< "Empty array\n";
        return;
    }
    cout << "Element\t\tValue" << endl;
    for (int i=0;i<a.size;i++) 
      cout << i << "\t\t" << a.p[ i ] << endl;
}
