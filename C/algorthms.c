
//https://www.w3schools.in/c-tutorial/recursion/
#include<stdio.h>
#include "funks.h"
int rec(int a)
{
	a++;
	printf("current depth= %d\n",a);
	return rec(a);
}
