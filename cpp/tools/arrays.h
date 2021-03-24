#ifndef __arrays
#define __arrays

#define OPTIMIZE

void selectionSort(int *a, const int len );
void selectionSort_rev(int *a, const int len );
void bubbleSort(int *a, const int len );
void bubbleSort_rev(int *a, const int len );

void printA(int a[],int len);
void random_array(int a[],int len,int min=0,int max=100);
#endif
