#include <unistd.h> // getuid
#include <stdio.h> // printf

int main()
{
    auto me=getuid();
	printf("%d\n",me);
	printf("%d\n",geteuid());
    if (getuid()) printf("%s", "You are not root!\n");
    else printf("%s", "OK, you are root.\n");
    return 0;
}
