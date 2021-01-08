#!/bin/sh
nproc=$(ps | wc -l)
echo $( ps )
echo "You are running $nproc processes"
echo "you are running $(( $( ps | wc -l) - 1)) procrsses"
exit 0
