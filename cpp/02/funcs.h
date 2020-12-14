#ifndef funcs__
#define funcs__

void ops(void);
int random_(int i);
long random_2();

class Array{
    public:
    int * p;
    int size;
};
Array creat_random_array(int size);
void print_array(Array a);

void charArrayTest(void);
void stringTest(void);

#endif