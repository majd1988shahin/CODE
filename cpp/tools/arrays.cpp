#include "arrays.h"
#include <iostream>
#include <iomanip>
#include <ctime>
using namespace std;
inline void swap(int *xp, int *yp)
{
    static int temp ;
    temp= *xp;
    *xp = *yp;
    *yp = temp;
}
void selectionSort( int *arr, int len)
{
	register int *p, *minp;
	// Pointer to array elements,
	int *last = arr + len-1; // pointer to the last element
	for( ; arr < last; ++arr)
	{
		minp = arr;
		// Search for minimum
		for( p = arr+1; p <= last; ++p) // starting with arr
			if( *minp > *p)
				minp = p;
		swap( arr, minp);
	}
}
void selectionSort_rev( int *arr, int len)
{
	register int *p, *minp;
	// Pointer to array elements,
	int *last = arr + len-1; // pointer to the last element
	for( ; arr < last; ++arr)
	{
		minp = arr;
		// Search for maximum
		for( p = arr+1; p <= last; ++p) // starting with arr
			if( *minp < *p)
				minp = p;
		swap( arr, minp);
	}
}
void bubbleSort(int *a, const int len )
{
	register int temp,*p,*q;
#ifdef OPTIMIZE
	register bool swapped;
#endif
	//const  len2=len;
	for(int i=0;i<len;i++)
	{
#ifdef OPTIMIZE
		swapped = false;
#endif
		p=a;
		q=a+1;
		for(int j=0;j<len-1;j++)
		{
			if(*p>*q)
				{
					swap(p,q);
#ifdef OPTIMIZE
					swapped = true;
#endif
				}
			p++;q++;
		}
#ifdef OPTIMIZE
		if (swapped == false)
		        break;
#endif
	}
}
void bubbleSort_rev(int *a, const int len )
{
	register int temp,*p,*q;
#ifdef OPTIMIZE
	register bool swapped;
#endif
	//const  len2=len;
	for(int i=0;i<len;i++)
	{
#ifdef OPTIMIZE
		swapped = false;
#endif
		p=a;
		q=a+1;
		for(int j=0;j<len-1;j++)
		{
			if(*p<*q)
				{
					swap(p,q);
#ifdef OPTIMIZE
					swapped = true;
#endif
				}
			p++;q++;
		}
#ifdef OPTIMIZE
		if (swapped == false)
		        break;
#endif
	}
}
void printA (int a[],int len)
{
	// len=sizeof(a)/sizeof(int);
	cout<<"Array=["<<endl;
	for(int i=0;i<len-1;i++)
		{
			std::cout<<std::setw(10)<<a[i]<<" , ";
			if(i%10 ==9)cout<<endl;
		}
	std::cout<<std::setw(10)<<a[len-1]<<"];\n";
}


void random_array(int a[],int len,int min,int max)
{
	srand((unsigned)time(NULL));
	for(int i=0;i<len;i++)
		a[i]=min+rand()%(1+max-min);
}
