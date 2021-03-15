import sys,os


g_rot13=lambda x: chr((ord(x)-65+13)%26 +65) if 65<=ord(x)<= 90 else None
k_rot13=lambda x: chr((ord(x)-97+13)%26 +97) if 97<=ord(x)<=122 else None

rot13=lambda x: g_rot13(x) or k_rot13(x) or x

print("a -> ",rot13("a"))
print("K -> ",rot13("X"))

print("".join(list(map(rot13,"Python ist toll!"))))

def main(argv):
    ifile=argv[1]
    ofile=argv[2]
    result=[]
    
    with open(ifile,"r") as f:
        result=list(map(rot13,f.read()))
        f.close()
    with open(ofile,"w+") as of:
        of.write("".join(result))
        print("".join(result))
        of.close()





if __name__ == '__main__':
    main(["/home/majd/PYP/19pyth10/PyPrgs/b04/b04A04.py", 
    "/home/majd/PYP/19pyth10/PyPrgs/b04/testText.txt" ,
    "/home/majd/PYP/19pyth10/PyPrgs/b04/Result_verschlusselung.txt"])