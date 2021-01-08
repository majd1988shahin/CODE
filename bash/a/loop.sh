#!/bin/bash
for f in $(find . -maxdepth 1 -name "*~")
do
	echo removing $f
	rm $f
done

#which is equivalent to:
#$ find . -name "*.o" -exec rm {} ’;’
