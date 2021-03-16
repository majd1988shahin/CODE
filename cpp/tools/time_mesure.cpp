
#include<iostream>
#ifdef CHRONO
#include <chrono>

#define TIME_MEASURE_INIT chrono::high_resolution_clock::time_point t1,t2;\
									               chrono::duration<double> __time_span;
#define TIME_MEASURE_START       __t1 = chrono::high_resolution_clock::now();
#define TIME_MEASURE_RESUALT 		__t2 = chrono::high_resolution_clock::now(); \
								        time_span = chrono::duration_cast<chrono::duration<double>>(t2 - __t1);\
								        std::cout << "It took me " << __time_span.count() << " seconds.\n";
#else
#include <ctime>
#define TIME_MEASURE_INIT  		clock_t __t1,__t2;\
                              double __t;
#define TIME_MEASURE_START      __t1 = clock();
#define TIME_MEASURE_RESUALT		__t2 = clock();\
								                __t= ((double)(__t2-__t1))/CLOCKS_PER_SEC;\
	                              std::cout<<"time_taken: "<<__t<<std::endl;
#endif//CHRONO
