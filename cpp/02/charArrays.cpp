#include <iostream>
#include "funcs.h"
#include <cstring>

using namespace std;
void charArrayTest(void)
{
    cout<<"String tests \n\n";
    char a[10*5]="Hello", b[]="World"; // a will be small for the next ops
    char c[15];
    int len;
    strcpy(c,a);
    cout<<"strcpy(c,a):"<<c<<endl;
    strcpy(c,b);
    cout<<"a + b :"<<c<<endl;

    cout<<"strcat(a,b): "<<strcat(a,b)<<endl;
    len=strlen(a);
    for(int i=0;i<10;i++)
        strcat(a,b);
    cout<<"strlen(a) :"<<strlen(a)<<endl;
}
