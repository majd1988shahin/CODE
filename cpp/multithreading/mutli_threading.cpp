// CPP program to demonstrate multithreading 
// using three different callables. 
#include <iostream> 
#include <thread>
#include <chrono>
#include <mutex>
using namespace std; 
std::mutex g_display_mutex;

int th=0;
// A dummy function 
void foo(int Z) 
{ 
	int thr=th;
	th++;
	for (int i = 0; i < Z; i++) { 
		{
		std::thread::id this_id = std::this_thread::get_id();
		g_display_mutex.lock();
		cout <<"thread "<<thr<<", thread ID: "<<this_id<<
		" Thread using function"
			" pointer as callable\n";
		g_display_mutex.unlock();
		std::this_thread::sleep_for(std::chrono::seconds(1));
			}
		 
	} 
} 

// A callable object 
class thread_obj { 
public: 
	void operator()(int x) 
	{ 
		int thr=th;
		th++;
		for (int i = 0; i < x; i++) 
			{
			std::thread::id this_id = std::this_thread::get_id();
			g_display_mutex.lock();
			cout <<"thread "<<thr 
			<< ", thread ID: "<<this_id<<
			" Thread using function object as callable\n"; 
			g_display_mutex.unlock();
			std::this_thread::sleep_for(std::chrono::seconds(1));
			}
	} 
}; 

int main() 
{ 
	cout << "Threads 1 and 2 and 3 "
		"operating independently" << endl; 

	// This thread is launched by using 
	// function pointer as callable 
	thread th1(foo, 3); 

	// This thread is launched by using 
	// function object as callable 
	thread th2(thread_obj(), 3); 

	// Define a Lambda Expression 
	auto f = [](int x) { 
			int thr=th;
			th++;
		for (int i = 0; i < x; i++) 
			{
			std::thread::id this_id = std::this_thread::get_id();
			g_display_mutex.lock();
			cout <<"thread "<<thr <<", thread ID: "<<this_id<<
			 " Thread using lambda expression as callable\n"; 
			g_display_mutex.unlock();
			std::this_thread::sleep_for(std::chrono::seconds(1));
			}
	}; 

	// This thread is launched by using 
	// lamda expression as callable 
	thread th3(f, 3); 

	// Wait for the threads to finish 
	// Wait for thread t1 to finish 
	th1.join(); 

	// Wait for thread t2 to finish 
	th2.join(); 

	// Wait for thread t3 to finish 
	th3.join(); 

	return 0; 
} 

