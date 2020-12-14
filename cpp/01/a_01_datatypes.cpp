//https://www.tutorialspoint.com/cplusplus/cpp_data_types.htm
#include <iostream>
#include <vector>
#include <string>
#include "func.h"
using namespace std;

//////////////////////////
void dataTypeSizes(void){


   cout << "Size of char : " << sizeof(char) << endl;
<<<<<<< HEAD
   cout << "Size of \"AB\" : " << sizeof("AB") << endl;
   cout << "Size of \'A\' : " << sizeof('A') << endl;
=======
>>>>>>> aae3d75c1a846f0cfdcd8f3430173ed0d283b9de
   cout << "Size of int : " << sizeof(int) << endl;
   cout << "Size of short int : " << sizeof(short int) << endl;
   cout << "Size of long int : " << sizeof(long int) << endl;
   cout << "Size of float : " << sizeof(float) << endl;
   cout << "Size of double : " << sizeof(double) << endl;
   cout << "Size of wchar_t : " << sizeof(wchar_t) << endl;
   
   return;

}
extern int ex;
///////////////////
typedef int feet;
enum color{blue,red=5, black};
int main()
{
    dataTypeSizes();
    feet a=010;
    color c=blue;
    cout << "Size of feet : " << sizeof(feet) << endl;
    cout<<"Size of Color : "<<sizeof(color)<<endl;
    cout<<"value of blue is "<<c<<endl;
    c=black;
    cout<<"value of black is "<<c<<endl;
    float f=0.1E-5;
    cout<<"float f : "<<f<<endl;
    ex=5;
    cout<< "extern var "<<ex<<endl;
    double av=average(3,4,3,2);
<<<<<<< HEAD
    cout<< "average 4 3 2 -> "<<av<<endl;
=======
    cout<< "average 5 3 2 "<<av<<endl;
>>>>>>> aae3d75c1a846f0cfdcd8f3430173ed0d283b9de
    vector<string> msg {"Hello", "C++", "World",  "from", "VS Code", "and the C++ extension!"};
    
    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout <<endl;
<<<<<<< HEAD
}
=======
}
>>>>>>> aae3d75c1a846f0cfdcd8f3430173ed0d283b9de
