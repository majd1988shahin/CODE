#include "funks.h"


void pointer_test(void)
{
   int  n = 20, *pntr;  /* actual and pointer variable declaration */
   pntr = &n;  /* store address of n in pointer variable*/
   printf("Address of n variable: 0x%lx\n", (unsigned long)&n  );
   pntr[0]=10;
   /* address stored in pointer variable */   
   printf("Address stored in pntr variable: 0x%lx\n", (unsigned long) pntr );

   /* access the value using the pointer */   
   printf("Value of *pntr variable: %d\n", *pntr );

}
