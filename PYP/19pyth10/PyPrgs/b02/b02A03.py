lis=[1,2,3]
lis[len(lis):]=[4]
unter=[4,5]
lis[1]=unter
unter[0]=7

print(lis)
print(unter)