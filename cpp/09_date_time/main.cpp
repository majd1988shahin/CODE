#include <iostream>
#include <string>
#include <iomanip>

#include <ctime>
class date
{
private:
	short day,mounth,year;
public:
	void init(short day, short mounth,short year);
	void init(void);
	void print(void);
};
void date::init(short day, short mounth,short year)
{	this->day=day;this->mounth=mounth;this->year=year;}
void date::init(void)
{
	std::time_t t=std::time(0);
	std::tm* now=std::localtime(&t);
	this->year	=now->tm_year+1900;
	this->mounth=now->tm_mon+1;
	this->day	=now->tm_mday;
}
void date::print(void)
{
	std::cout<<"date : "<<this->day<<'.'<<this->mounth<<'.'<<this->year<<std::endl;
}

using namespace std;

int main()
{
	date s;
	s.init();
	s.print();

return 0;
}



