///
#include<stdio.h>
#include "funks.h"

void test_array(void)
{
	int myArray[5];
	int n = 0;

	// Initializing elements of array seperately
	for(n=0;n<sizeof(myArray)/sizeof(myArray[0]);n++)
	{
	  myArray[n] = n; 
	}
	printf("\rtest_array: OK\n");

}
