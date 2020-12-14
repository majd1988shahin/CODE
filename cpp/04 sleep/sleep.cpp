#include <chrono>
#include <thread>
#include <iostream>
int main() {
    using namespace std::this_thread;     // sleep_for, sleep_until
    using namespace std::chrono_literals; // ns, us, ms, s, h, etc.
    using std::chrono::system_clock;
	
	//c++ 14
    	sleep_for(10ns);
	int s=10;
	std::cout<<"sleep a\n";
    	sleep_until(system_clock::now() + 2s);
	std::cout<<"sleep b\n";
	/*
		//c++ 11
	    sleep_for(nanoseconds(10));
	    sleep_until(system_clock::now() + seconds(1));
	*/
}
