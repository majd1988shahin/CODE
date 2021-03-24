#include<iostream>
using namespace std;
int main(int argc,char * argv[],char * env[])
{
  cout<< "hello World"<<endl;
  for(int i=0;i<argc;i++)
    cout<<"argv["<<i<<"] : "<<argv[i]<<endl;
  cout<<"_______________"<<endl;
  for (int i=0;env[i];i++)
    cout<<"env["<<i<<"] : "<<env[i]<<endl;
  return 0;
}
