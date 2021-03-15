import sys
import os
filename=os.getcwd()+"/samples/sample0.cpp"
s= open(filename)
    
code =list(s.read())
#print(contents)
A=["{","[","(",'"']
B={"{":"}","[":"]","(":")",'"':'"'}
i=0
Error =False
Error_num=None 
def search(code,i):
    global Error
    global Error_num
    K=B[code[i]]
    i=i+1
    while i<len(code):         
        if code[i]==K:
            return i+1
        
        elif (code[i] in B.values() )and K!='"' and code[i]!='"': 
            Error=True
            Error_num=i
            print("Error",code[i]," ist extra")
            i=i+1
        elif (code[i] in A) and K!='"':
            i=search(code,i)
        else :
            i=i+1
        
    Error =True
    Error_num=i-1
    #print ("Error",code[i-1]," did not closed")
    return len(code)

while i< len(code):
    if code[i] in B.values() and code[i]!='"':
        Error =True
        Error_num=i
        print("Error :",code[i] ," is extra")
    if code[i] in A:
        i=search(code,i)
    else:
        i=i+1
    
print("Error :",Error)
print("Error Num :",Error_num)
    


