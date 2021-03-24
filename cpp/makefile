CC = g++
files = main.o #./tools/read_lines_from_file.o

main: $(files)
	$(CC) $(files) -std=c++17 -lstdc++fs -o main
	echo "main"
	#clean
	rm -rf $(files)


main.o: main.cpp
	$(CC) main.cpp -c -std=c++17 -lstdc++fs -o main.o
#./tools/read_lines_from_file.o: ./tools/read_lines_from_file.cpp
