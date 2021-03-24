#include "read_lines_from_file.h"
std::vector<std::string> read_lines(std::string f)
{
	std::vector<std::string> res;
	std::ifstream file(f);
	if (! file.is_open())
	{
		std::cerr<<"file not exists :"<<f<<std::endl;
		return res;
	}
	std::string line;
    while (getline(file, line))
	{

		//std::cout << line << "\n";
		res.push_back(line);
		
	}
	return res;
}
