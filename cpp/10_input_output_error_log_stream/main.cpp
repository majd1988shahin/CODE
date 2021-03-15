/*
	
	./a.out 2> a.txt
		cerr and clog will be written in a.txt

*/
#include <iostream>
 
using namespace std;
 
int main() {
   char name[50];
 
   cout << "Please enter your name: ";
   cin >> name;
   cout << "Your name is: " << name << endl;
   
      char str[] = "Unable to read....";
 
   cerr << "Error message : " << str << endl;
   
   clog << "Error message : " << str << endl;
   return 0;
 
}
