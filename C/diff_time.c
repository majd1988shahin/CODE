#include <time.h> 
#include <stdio.h> 
#include "funks.h"
static clock_t __t;
static int __t_inuse=0;

int timer_start(void)
{
	//if (__t_inuse==0)
	//{
	//	__t_inuse=1;
		__t=clock();
		return 0;
	//}
	//return 1;
}

double timer_stop_get(void)
{
	//if (__t_inuse==0)
	//	return 0;
	__t=clock()-__t;
	//__t_inuse=0;
	return ((double)__t)/CLOCKS_PER_SEC; 
}

void test_diff_time(void)
{
	if(timer_start()==1)
		printf("\rError in timer\n");
	/*char c ;getc(&c); //Use to get one character input from user, and it will not be printed on screen.
	printf("adksfnasdjfasdfjasdfnjasdbfjasdfasdbfjadbfajdbfjasdbfhjasdbf\n");
*/
	int i,j,k;
	for(k=0;k<351;k++)
	for (i=0;i<1000;i++)
	 for (j=0;j<1000;j++)
	;
	double time=timer_stop_get();
	printf("eclepsed time = %f\n",time);
}
