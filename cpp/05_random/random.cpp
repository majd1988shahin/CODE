#include <iostream>
#include<ctime>
#include<cstdlib>

using namespace std;

int main()
{
	//srand((unsigned)time(NULL));
	for (int i=0;i<10;i++)
	{
		cout<<"random number : "<<rand()<<endl;
	}

	return 0;
}
