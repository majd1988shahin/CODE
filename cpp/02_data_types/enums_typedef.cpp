#include <iostream>
using namespace std;

enum color { red, green, blue } ;
typedef float volt;
float current (float V, float R)
{
	return V/R;
}
int main()
{
	color c =blue;
	cout<< "size of enum ="<<sizeof(c)<<endl;
	cout<< "index of the secound element in enum : "<<c<<endl;
	volt v=5.0f;
	float r=1.0f;
	cout<< current(v,r)<<endl;
	cout<<'\u02C0'<<endl;
	return 0;
}

