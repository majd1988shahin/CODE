#ifndef __funks__
#define __funks__
#include <stdio.h> 
#include <limits.h>
int timer_start(void);
double timer_stop_get(void);
void test_diff_time(void);

//////
void test_array(void);
/////
void c_string_test1(void);
void c_string_take_data_from(void); /////!!!!!!!
/////
//char* concat2(char *s1, char *s2);
//size_t get_length_from_pointer(char* a);
char* concat(int count, ...);
////
void pointer_test(void);

////
void dynamic_memory_test(void);
////
void struct_test(void);
///
void open_close_file_test(char * f);
int read_file(char * f);
void writ_to_file(char *f);
void read_data_from_file(char * f);
//////
static  char cwd[PATH_MAX];
//void save_current_directory(void);
////////
int rec(int a);
////////
/*separating a string
  char str[] ="- This, a sample string.";
  char ** sen;
  char* sep=".-,; ";
int size=string_seprate(str,sep,&sen);
*/
int string_seprate(char * src,char* sep,char *** res);

////multithreading
void thread_test(void);
#endif
