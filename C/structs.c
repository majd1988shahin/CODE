#include<stdio.h>
#include<string.h>
#include<stdint.h> 
/* stdint.h-> uint32_t*/
#include "funks.h"

struct Player
{
char first_name[20];
char last_name[20];
uint32_t  score;
};

void struct_test(void)
{
	struct Player majd;
	strcpy(majd.first_name,"majd");
	strcpy(majd.last_name,"shahin");
	majd.score=10;
	
	printf("player name: %s %s\n",majd.first_name,majd.last_name);
	printf("player score: %u \n",majd.score);

}
