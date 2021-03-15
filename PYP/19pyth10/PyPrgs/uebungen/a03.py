import ctypes
import string
cs=string.ascii_letters.encode("ascii")
arr=(ctypes.c_char*53)(*cs)
libc=ctypes.cdll.LoadLibrary("libc.so.6")
libc.printf(arr)

def maxsub_py(lis):
    max_sum, start, end = 0, 0, -1
    n = len(lis)

    for i in range(n):
        sum = 0
        for j in range(i, n): 
            sum += lis[j] # sum == sum(lis[i:(j+1)])
            if sum > max_sum:
                max_sum = sum
                start, end = i, j
    return max_sum, start, end

import random
import time
lis=list(range(-3000,3000))
random.shuffle(lis)
print("\n")
a=time.time()
print(maxsub_py(lis))
b=time.time()
print("python3 Maxsub time ",b-a)#python3 Maxsub time  2.9569473266601562


###########


def get_cmaxsub(): 
    path = os.path.join(os.getcwd(), "maxsub_c.so")
    clib = ctypes.cdll.LoadLibrary(path)
    c_int_p = ctypes.POINTER(ctypes.c_int)
    c_int = ctypes.c_int # shorter
    argtypes = [c_int_p, c_int, c_int_p, c_int_p]
    clib.maxsub_c.argtypes = argtypes
    return clib.maxsub_c
import os

def maxsubc(lis):
    n=len(lis)
    arr=(ctypes.c_int*n)(*lis)
    start, end =ctypes.c_int(0),ctypes.c_int(-1)
    cf=get_cmaxsub()
    max_sum=cf(arr,n,ctypes.byref(start),ctypes.byref(end))
    return max_sum,start.value,end.value
a=time.time()
print(maxsubc(lis))
b=time.time()
print("c funktion time ",b-a)#c funktion time  0.11506342887878418