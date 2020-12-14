/*
gcc main.c -o main.o
./main.o
*/
#include <stdlib.h>
#include <stdarg.h>       // va_*
#include <string.h>
#include <stdio.h>
#include<math.h>
void pi(int a){printf("%d\n",a);}
void pf(float a){printf("%f\n",a);}
#define A printf("done\n")
#define pr printf

typedef int I;
typedef short S;
typedef char C;
typedef float F;
<<<<<<< HEAD
#include "funks.h"
// #define pp(int) pi(int)

struct data
{
int x;
int y;
int z;
int w;
};

struct database
{
int size;
struct data ** ptr;
};
int add_data(int a,int b, struct database *db)
{

	struct data *d=malloc(sizeof(struct data));
	d->x=a;d->y=b; d->z=0;d->w=db->size;
	db->ptr=realloc(db->ptr,(1+db->size)*sizeof(struct data *));
	db->size++;
	return 0;
}
void print_data(struct data * d)
{
	A;
	printf("[%d , %d , %d , %d]\n",d->x,d->y,d->z,d->w);
}

struct dy_int_array
{
int size;
int *ptr;
};
void add_to_array(struct dy_int_array *da,int d)
{
	da->ptr=realloc(da->ptr,(1+da->size)*sizeof(int));
	da->ptr[da->size]=d;
	da->size++;
}
void test()
{
struct dy_int_array da;
da.size=0;da.ptr=NULL;
//add_to_array(&da,33);
char c[20];
int temp=0;
for (int i=0;i<30;i++)
{
	scanf("%d",&temp);
	if (temp<0) break;
	add_to_array(&da,temp);

}
printf("Array size = %d\n",sizeof(da));
printf("Array pinter size = %d\n",sizeof(da.ptr));
for (int i=0;i<da.size;i++)
pi(da.ptr[i]);
=======
//#include "funks.h"
// #define pp(int) pi(int)

struct ss{
int a;
//struct ss *p;
};

void test()
{
   char *s = "-230kk9.12E-15";
    float x = atof(s);     /* x = -2309.12E-15 */
 
    printf("x = %.4e\n",x);
>>>>>>> aae3d75c1a846f0cfdcd8f3430173ed0d283b9de

}



int main()
{
	printf("----------------------\nHello, World!\a\n");
	//getchar(); //Use to get one character input from user, and it will not be printed on screen.
	//test_diff_time();
	//test_array();
	//c_string_test1();
	//pointer_test();
	//dynamic_memory_test();
	//struct_test();
	char f[10]="hi.txt";
	//open_close_file_test(f);
	//int lines=read_file(f);
	//printf("total lines %d\n",lines);
	//c_string_take_data_from();
	//writ_to_file(f);
	//read_data_from_file(f);
	//rec(0);
<<<<<<< HEAD
	//test();
	thread_test();
	printf("End\n");
=======
	test();
>>>>>>> aae3d75c1a846f0cfdcd8f3430173ed0d283b9de
	return 0;
}
