#include <iostream>
#include <vector>

#include <experimental/filesystem>


#include <unistd.h>

using namespace std;
namespace fs=  std::experimental::filesystem;

int main(int argc,char * argv[],char * env[])
{
    string s= fs::current_path();
cout<<s<<endl;
cout<<"hello world "<<endl;
  return 0;
}
