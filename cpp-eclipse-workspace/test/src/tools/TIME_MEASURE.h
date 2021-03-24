#ifndef TIME_MEASURE
#define TIME_MEASURE
#include<iostream>

#include <ctime>
#define TIME_MEASURE_INIT  		clock_t __t1,__t2;\
                              double __t;
#define TIME_MEASURE_START      __t1 = clock();
#define TIME_MEASURE_RESUALT		__t2 = clock();\
								                __t= ((double)(__t2-__t1))/CLOCKS_PER_SEC;\
	                              std::cout<<"time_taken: "<<__t<<std::endl;

#endif //TIME_MEASURE
