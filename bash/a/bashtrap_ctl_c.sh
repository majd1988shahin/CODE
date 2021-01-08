#!/bin/bash

trap bashtrap INT
# bash clear screen command
# bash trap function is executed when CTRL-C is pressed:
# bash prints message => Executing bash trap subrutine !
bashtrap()
{
	echo "CTRL+C Detected !...executing bash trap !"
	exit
}
for a in `seq 1 10` ; do # !!!! shift+`+` »`   /// it is not ' 
	echo "$a/10 to Exit."
	sleep 1 ;
done
