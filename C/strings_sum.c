#include <stdlib.h>
#include <stdarg.h>       // va_*
#include <string.h>
#include "funks.h"

//https://www.tutorialspoint.com/c_standard_library/c_function_sprintf.htm
//int sprintf(char *str, const char *format, ...)
char* concat(int count, ...)
{
    va_list ap;
    int i;

    // Find required length to store merged string
    int len = 1; // room for NULL
    va_start(ap, count);
    for(i=0 ; i<count ; i++)
        len += strlen(va_arg(ap, char*));
    va_end(ap);

    // Allocate memory to concat strings
    char *merged = calloc(sizeof(char),len);
    int null_pos = 0;

    // Actually concatenate strings
    va_start(ap, count);
    for(i=0 ; i<count ; i++)
    {
        char *s = va_arg(ap, char*);
        strcpy(merged+null_pos, s);
        null_pos += strlen(s);
    }
    va_end(ap);

    return merged;
}
/*size_t get_length_from_pointer(char* a)
{
	size_t size=0;
	while(a[size]) 
	{
		size++;
		if(size==100)
		{
			printf("error in get_length_from_pointer\n");
			return 0;
		}
	}
	return size;
}
char* concat2( char *s1,  char *s2)
{
    printf("in concat2\n");
    size_t len1 = get_length_from_pointer(s1);
	printf("size of s1= %d\n",len1);
    size_t len2 = get_length_from_pointer(s2);
	printf("size of s2= %d\n",len2);
    char *result = malloc(len1 + len2 + 1); // +1 for the null-terminator
    // in real code you would check for errors in malloc here
    memcpy(result, s1, len1);
    memcpy(result + len1, s2, len2 + 1); // +1 to copy the null-terminator
    return result;
}
*/
