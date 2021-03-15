#include <iostream>
using namespace std;

void f(int *a)
{
	*a=5;
}
int main()
{
	int a=50;
	f(&a);
	cout<<a<<endl;
	cout<<&a<<endl;
	register int b=50;
	f(&b);
	cout<<b<<endl;
	cout<<&b<<endl;

	volatile int c=50;
	//f(&c);
	cout<<c<<endl;
	cout<<&c<<endl;

	volatile int d=50;
	//f(&c);
	cout<<d<<endl;
	cout<<&d<<endl;

	return 0;
}
