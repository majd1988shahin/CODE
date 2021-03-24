#include <iostream>
#include <string>
#include <cstring>
#include <ctime>
//void printA(int a[],int len);
#include "tools/TIME_MEASURE.h"
#include "tools/filesystem_apps.h"
#include "tools/arrays.h"
#include<unistd.h>
#include <iomanip>
#include <fstream>///!!!
using namespace std;
class A
{
private:
	int n;
public:

	A(int s){this->n=s;}
	friend A& operator ++(A);
	friend A& operator ++(A,int);
};
A& operator ++(A a){
	a.n++;
	cout<<"++A "<<a.n<<endl;
}
A& operator ++(A a,int){
	a.n++;
	cout<<"A++ "<<a.n<<endl;

}
int main()
{
	A a(3);
	++a;
	a++;
	return 0;
}
