#include <iostream>
#include <string>
#include <vector>
//#include <memory>
#include "tools/Storge.hpp"


int main()
{
	Storge<int> a(2);
	cout<<sizeof(a)<<endl;
	for(int i=0;i<100001;i++)
		a.push(i);
	a[3]=0;
	cout<<a[3]<<endl;
	cout<<sizeof(a)<<endl<<a.SIZE<<endl<<a.i;


	return 0;
}
