#!/bin/bash
echo "Do you want to destroy your entire file system?"
read response

case "$response" in ### $response without ""
   "yes")              echo "I hope you know what you are doing!" ;;
   "no")              echo "You have some comon sense!" ;;
   "y" | "Y" | "YES" ) echo "I hope you know what you are doing!" ;;
                       
   "n" | "N" | "NO" )  echo "You have some comon sense!" ;;
   *   )               echo "You have to give an answer!" ;;
esac

echo "What is your preferred programming / scripting language 1-5"

read res;
#simple case bash structure
# note in this case $case is variable and does not have to
# be named case this is just an example
case $res in
    1) echo "You selected bash" 	;;
    2) echo "You selected perl";;
    3) echo "You selected phyton";;
    4) echo "You selected c++";;
    5) exit
esac 
