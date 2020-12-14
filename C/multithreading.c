#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sched.h>
#include <unistd.h>
#include "funks.h"
pthread_mutex_t lock;
// Let us create a global variable to change it in threads 
volatile int g = 0; 

// The function to be executed by all threads 
void *myThreadFun(void *vargp) 
{ 
	
	// Store the value argument passed to this thread 
	int *myid = (int *)vargp; 

	// Let us create a static variable to observe its changes 
	static int n=0;
	n++;
	int l=n;
	// Change static and global variables 
	

	// Print the argument, static and global variables 
	for(int i=0;i<5;i++){
	pthread_mutex_lock(&lock);
	++g; 
	printf("Thread ID: %u, local: %u, Global: %u\n", *myid, l, g); 
	pthread_mutex_unlock(&lock);
	usleep(30);
	 }
	pthread_exit(NULL);// like return
	//pthread_detach(myid);// destroy the thread
} 

void thread_test()
{ 
	int i; 
	pthread_t tid[3]; 

	// Let us create three threads 
	for (i = 0; i < 3; i++) 
	{
		pthread_create(&tid[i], NULL, myThreadFun, (void *)&tid[i]); 
	}
	for (i = 0; i < 3; i++) 
	{
		pthread_join(tid[i],NULL);
	}
	/* if join excuted after the creat exactly it will waits this thread to be 
		finished befor creating a new one !!*/
	//thats why all threads have to start before joining them
	//	pthread_exit(NULL);  //
	/* waits for all threads and exit the main_thread > the reamining
	 instructions will not excuted !!*/

	pthread_mutex_destroy(&lock);
	return;
	
} 

