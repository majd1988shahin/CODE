#include <stdio.h>
#include <unistd.h>

//#include <linux.h>
int main (int argc, char ** argv)
{
	fprintf(stdout, "\aBeep!\n" );
	for (int i=0;i<1;i++)
	{
		printf("\a");

	}
	beep(1000,1000);
	return 0;
}
