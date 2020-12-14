#include"funks.h"

/*
char name[6] = {'C', 'l', 'o', 'u', 'd', '\0'};
char name[] = "Cloud";

*/

void c_string_test1(void)
{
   char name[6] = {'C', 'l', 'o', 'u', 'd', '\0'};

   printf("Tutorials %s\n", name );

}

void c_string_take_data_from(void)
{

	char data[256];
	fgets(data,sizeof(data),stdin);
	printf("data= %s\n",data);
	int day, year;
	char weekday[20], month[20];
	sscanf( data, "%s %s %d  %d", weekday, month, &day, &year );

   	printf("%s %d, %d = %s\n", month, day, year, weekday );
}

