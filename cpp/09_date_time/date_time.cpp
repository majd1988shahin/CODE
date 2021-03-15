#include <iostream>
#include <ctime>

using namespace std;
void get_time();

int main() {
   // current date/time based on current system
   time_t now = time(0);
   cout<<"size of time_t : "<<sizeof(now)<<endl;
   // convert now to string form
   char* dt = ctime(&now);

   cout << "The local date and time is: " << dt << endl;

   // convert now to tm struct for UTC
   tm *gmtm = gmtime(&now);
   dt = asctime(gmtm);
   cout << "The UTC date and time is:"<< dt << endl;
   get_time();
}

void get_time()
{
	   // current date/time based on current system
   time_t now = time(0);

   cout << "Number of sec since January 1,1970 is:: " << now << endl;

//   tm *t = localtime(&now);
   tm *t = gmtime(&now);//UTC

   // print various components of tm structure.
   cout << "Year:" << 1900 + t->tm_year<<endl;
   cout << "Month: "<< 1 + t->tm_mon<< endl;
   cout << "Day: "<< t->tm_mday << endl;
   cout << "Time: "<< t->tm_hour << ":";
   cout << t->tm_min << ":";
   cout << t->tm_sec << endl;

}
