#include "filesystem_apps.h"


using namespace std;
namespace fs=  std::experimental::filesystem;
vector<std::string> read_file(std::string fName, bool print)
{
	vector<string> res;
	if(fs::is_regular_file(fName))
		{if(print)cout<<"file : " <<fName<<" (exists!)"<<endl;}
	else
	{
		if(print)cout<<"file : " <<fName<<" (not exists!!)"<<endl;
		return res;
	}
	std::ifstream f(fName);
	std::string s;
	while(getline(f,s))
	{
		res.push_back(s);
		if(print)
			cout<<s<<endl;
	}
	return res;
}
void show_infos(std::string path)
{

	fs::path d;
	if (path == "\n")
		d= fs::current_path();
	else
		d=fs::path(path);

	cout << "current path : " << d<< endl;
	cout<<"files and folders in the current path : "<<endl;
	for (const auto & entry : fs::directory_iterator(d))
	{
		fs::path s=entry.path();
		if(fs::is_directory(s))cout<<"folder: ";
		else cout<<"file  : ";
		cout << entry.path() << endl;
	}
}

path_infos::path_infos(string path, bool print)
{
	fs::path d;
		if (path == "\n")
			d= fs::current_path();
		else
		{
			d=fs::path(path);
			if(! fs::is_directory(d))
			{
				if(print) cerr<<path<<" is not folder"<<endl;
				return ;
			}
		}


	for (const auto & entry : fs::directory_iterator(d))
	{
		fs::path s=entry.path();
		if(fs::is_directory(s))
		   this->folders.push_back(s);
		else this->files.push_back(s);
	}
	if(print)
	{
		for( auto part : this->files)
			cout<<"file  : "<<part<<endl;
		for( auto part : this->folders)
			cout<<"folder: "<<part<<endl;

	}
}
#include <sstream>

std::vector<std::string> files_filter(std::vector<std::string> vs,std::string filters)
{
	std::vector<std::string> res;
	std::vector<std::string> F;
	std::stringstream  ss(filters);
	std::string temp;

	for(auto s : vs)
	{
		while(std::getline(ss, temp,','))
		{
			if(fs::path(s).extension()==temp)
			{
				res.push_back(s);
				break;
			}
		}
	}
	return res;
}


