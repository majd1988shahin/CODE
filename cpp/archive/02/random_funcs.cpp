#include <iostream>
#include <ctime>
#include <cstdlib>
#include "funcs.h"
long random_2()
{
    return random();
}
int random_(int i)
{

 
   // set the seed
   srand( (unsigned)time( NULL ) +i);

    return rand();

}