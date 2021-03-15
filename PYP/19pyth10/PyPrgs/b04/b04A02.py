
B={}
N=0

while len(B)==0:
    N=N+1
    n=list(range(1,N))
    a=set([tuple(sorted((x,y))) for x in n for y in n[:x]])
    B=set([tuple(sorted((x,y))) for x in a for y in a 
        if x[0]**3+x[1]**3==y[0]**3+y[1]**3 and not x[0]==y[0]])
 
print("Minimum ist ",N-1)
print(B)

print("für Granz N=40 (es dauert !!)")
n=list(range(1,40+1))

#print(n)
a=set([tuple(sorted((x,y))) for x in n for y in n[:x]])
B=set([tuple(sorted((x,y))) for x in a for y in a if x[0]**3+x[1]**3==y[0]**3+y[1]**3 and not x[0]==y[0]])

for x in B:
    print(x[0][0],"^3+",x[0][1],"^3=",x[1][0],"^3+",x[1][1],"^3=",x[0][0]**3+x[0][1]**3)