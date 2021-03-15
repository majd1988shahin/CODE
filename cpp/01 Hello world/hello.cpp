#include <iostream>
using namespace std ;

int main()
{
	cout<<"Hello World\n";
	float b=1742.54f;
	float s=0.005f;
	float r;
	cout<< "enter the mothly mony"<<endl;
	cin>>r;
	float sum=0;
	while(1)
	{
		cout<<s*b<<endl;
		sum+=s*b;
		if(b>r)
			b-=r;
		else {b=0;break;}

	}
	cout<<"------------------\n";
	cout<<sum<<endl;
	return 0;
}
