#include <unistd.h>
#include <stdio.h>
#include <limits.h>
#include "funks.h"
// the result cannot be transfered directly
// for windows GetCurrentDir or _getcwd
//
//https://stackoverflow.com/questions/298510/how-to-get-the-current-directory-in-a-c-program
/*
void save_current_directory(void)
{

//

   if (getcwd(cwd, sizeof(cwd)) != NULL) 
   {
	size_t size=	get_length_from_pointer(cwd);
	
       printf("Current working dir: %s\n", cwd);
 	return ;
   } 
   else 
   {
       perror("getcwd() error");
       return ;
   }
   

}
*/
