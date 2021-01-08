#!/bin/bash
B='backup.tar.gz'
echo ' ' > backups.txt

for sd in $(find $1 -maxdepth 1 -type d -not -name ".*" -not -name "."  ) ; do
if [ "$sd" = "$1" ] ; then continue  ; fi 
#echo "sd : $sd"
#echo "basename : $( basename $sd )"
x="$2/$( basename $sd )"
#echo "folder_backup : $x"
#echo "$x" #>>  /mnt/AC36685336682096/Code/bash/a/backups.txt
if [ -e "$x" ] ; then a=1 ; else
mkdir "$x" ;
fi
#echo "$x/$B" ;
tar -czfP "$x/$B" "$sd" 
done

