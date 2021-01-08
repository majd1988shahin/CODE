#!/bin/bash
#https://unix.stackexchange.com/questions/129072/whats-the-difference-between-and
echo "command name $0"
echo "command argument 1 $1"



i=1
echo "number of args $#"
echo ---------------------
echo 'using $*'

echo "all args $*"
for a in $*;
do echo "arg[$i] = $a"
i=$((i+1));
done
echo ---------------------

i=1
echo 'using $@'
echo "all args $@"
for b in $@;
do echo "arg[$i] = $b"
i=$((i+1));
done
echo ---------------------
i=1
echo 'using "$@"'
echo "all args $@"
for b in "$@";
do echo "arg[$i] = $b"
i=$((i+1));
done
