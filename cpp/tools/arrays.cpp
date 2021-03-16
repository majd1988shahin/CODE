void selectionSort(int *a, const int len )
{
	int temp,*p,*q;
	//const  len2=len;
	for(int i=0;i<len;i++)
	{
		p=a;
		q=a+1;
		for(int j=0;j<len-1;j++)
		{
			if(*p<*q)
			{
				temp=*p;
				*p=*q;
				*q=temp;
			}
			p++;q++;
		}
	}
}
void printA(int a[],int len)
{
	// len=sizeof(a)/sizeof(int);
	std::cout<<"Array=[";
	for(int i=0;i<len-1;i++)
		std::cout<<a[i]<<" , ";
	std::cout<<a[len-1]<<"];\n";
}

#include <ctime>
void random_array(int a[],int min,int max,int len)
{
	srand((unsigned)time(NULL));
	for(int i=0;i<len;i++)
		a[i]=min+rand()%(1+max-min);
}
