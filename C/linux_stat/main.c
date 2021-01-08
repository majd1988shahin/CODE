       #include <sys/types.h>
       #include <sys/stat.h>
       #include <unistd.h>
		#include<stdio.h>
int main()
{
///////////////
struct stat s;
char * name="/mnt/AC36685336682096/Code/C/linux_stat";
int res=stat(name,&s);
printf("main.c stat is : %ld\n",s.st_size);

return 0;


}
