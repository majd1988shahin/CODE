/*
https://www.w3schools.in/c-tutorial/file-handling/fscanf/
--fopen		Opens a file.
FILE *fopen( const char * filePath, const char * mode );
r	Opens an existing text file.
w	Opens a text file for writing if the file doesn't exist then a new file is created.
a	Opens a text file for appending(writing at the end of existing file) and create the file if it does not exist.
r+	Opens a text file for reading and writing.
w+	Open for reading and writing and create the file if it does not exist. If the file exists then make it blank.
a+	Open for reading and appending and create the file if it does not exist. The reading will start from the beginning, but writing can only be appended.
--------------------------------------------------------------
--fclose	Closes a file.
--getc		Reads a character from a file
--putc		Writes a character to a file
--getw		Read integer
--putw		Write an integer
--fprintf	Prints formatted output to a file
--fscanf	Reads formatted input from a file
--fgets		Read string of characters from a file
--fputs		Write string of characters to file
--feof		Detects end-of-file marker in a file
*/

#include<stdio.h>
#include <unistd.h>
#include"funks.h"
void open_close_file_test(char * f)
{
	FILE * fp;
	//save_current_directory();
	getcwd(cwd, sizeof(cwd));
	char * fullName=concat(3,cwd,"/",f);
	fp=fopen(fullName,"w");
	if(fp!= NULL)
		printf("file \"%s\" is opend\n",fullName);
	else
		printf("cannot open file\n");
	fclose(fp);
	
}
int read_file(char * f)
{
  int lines=0;
  FILE * fp;
  getcwd(cwd, sizeof(cwd));
  char * fullName=concat(3,cwd,"/",f);
  fp=fopen(fullName, "r");
  int ch = getc(fp);
   printf("-------------------\n");
  while (ch != EOF)
  {
    /* To display the contents of the file on the screen */    
    putchar(ch);
    if(ch=='\n')
       lines++;
    ch = getc(fp);
  }
   printf("\n-------------------\n");
  if (feof(fp))
     printf("\nReached the end of file.\n");
  else
     printf("\nSomething gone wrong.\n");
  fclose(fp);
  return lines;
}
void writ_to_file(char *f)
{
  char ch;
  FILE * fp;
  getcwd(cwd, sizeof(cwd));
  char * fullName=concat(3,cwd,"/",f);
  fp=fopen(fullName, "w");
  for (ch = 'D' ; ch <= 'S' ; ch++) {
    putc (ch , fp);
    }
  fprintf(fp,"\n%d",55);///////********** best way *******
  fclose (fp);
}
void read_data_from_file(char * f)
{

  FILE * fp;
  getcwd(cwd, sizeof(cwd));
  char * fullName=concat(3,cwd,"/",f);
  fp=fopen(fullName, "r");
  char s1[20],s2[20];
  int n;
/*reading 
majd shahin 1988
ola shahin 1990
*/
  fscanf(fp,"%s %s %d",s1,s2,&n);
  printf("s1: %s\ns2: %s\nn: %d\n",s1,s2,n);
  fscanf(fp,"%s %s %d",s1,s2,&n);
  printf("s1: %s\ns2: %s\nn: %d\n",s1,s2,n);
}
