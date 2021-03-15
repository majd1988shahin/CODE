#include <iostream>
#include <string>
#include <iomanip>
#include <cstring>
#include <ctime>
class Lights
{
	public:
	enum State { off, red, green, amber }; // Enumeration for class
	State state;
	int s[9];
};
using namespace std;

int main()
{
	Lights s[10];
	cout<<sizeof(s);
return 0;
}


