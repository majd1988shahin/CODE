#include <iostream>
using namespace std;
bool f(bool b)
{
	static int a=0;
	
	cout<<a++<<endl;
	return b;
}

int main()
{
	if (f(1)||f(0)||f(1));
	printf("done\n");
	return 0;
}

