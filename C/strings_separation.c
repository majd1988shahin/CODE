#include <stdlib.h>
#include <stdarg.h>       // va_*
#include <string.h>
#include "funks.h"

int string_seprate(char * src,char *sep,char *** res)
{
	printf("%s\n",src);
	//const char* sep=".-, ";
	int size;
	int n=0;
	char* word;
	char** sen=malloc(30*sizeof(char*));
	word=strtok(src,sep);
	while(word!=NULL)
	{	
		size=strlen(word)+1;
		//printf("size= %d\n",size);
		sen[n]=malloc(size*sizeof(char));
		strcpy(sen[n],word);
		
		printf("%s\n",sen[n]);
		word=strtok(NULL,sep);
		n++;
	}
*res=sen;
return n;

}

