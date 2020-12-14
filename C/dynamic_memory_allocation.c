/*
 stdlib.h
 malloc function does not initialize the memory
 calloc () allocates memory for zero-initializes.
 realloc function modifies the allocated memory size by malloc and calloc
 functions to new size.
	If enough space doesn't exist in the memory of current block to extend, 
	a new block is allocated for the full size of reallocation, then copies
	the existing data to the new block and then frees the old block.

*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#include "funks.h"
void dynamic_memory_test(void)
{

  char *mem_alloc;
  /* memory allocated dynamically */
  mem_alloc = malloc( 20 * sizeof(char) );

  if( mem_alloc == NULL )
  {      
	printf("Couldn't able to allocate requested memory\n");
  }
  else
  {      
	strcpy( mem_alloc,"w3schools.in");
  }

  printf("Dynamically allocated memory content  :  %s\n", mem_alloc );
  mem_alloc=realloc(mem_alloc,100*sizeof(char));

  if( mem_alloc == NULL )
  {      
	printf("Couldn't able to allocate requested memory\n");
  }
  else
  {      
	strcpy( mem_alloc,"space is extended upto 100 characters");
  }

  printf("Resized memory : %s\n", mem_alloc );
  free(mem_alloc);   
}

