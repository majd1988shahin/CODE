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
