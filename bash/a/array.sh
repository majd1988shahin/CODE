#!/bin/bash
set -e
array=( one two three )
n=${#array[@]}
for (( i=0; i< $n ; i++)); do
	echo ${array[${i}]} ;
done

for i in `seq 0 $n`; do
	echo ${array[${i}]} ;
done
echo \a
