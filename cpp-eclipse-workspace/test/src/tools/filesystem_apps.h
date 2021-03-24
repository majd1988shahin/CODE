#ifndef filesystem_apps
#define filesystem_apps
#include <iostream>
#include <experimental/filesystem>
#include <string>
#include <fstream>
#include <vector>
class path_infos
{
public:
	std::vector<std::string> files;
	std::vector<std::string> folders;
	path_infos(std::string = "\n",bool print=true);
};
void show_infos(std::string path="\n");
std::vector <std::string> read_file(std::string fName="\n", bool print=true);
std::vector<std::string> files_filter(std::vector<std::string> vs,std::string filters=".c,.cpp,.txt");

#endif
