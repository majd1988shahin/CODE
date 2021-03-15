a=list(zip((1,2,3,4), (5,6), (7,8)))
print (a)

unzip=lambda a=[()]: (zip(*a))

print(*unzip(a))
# def unzip2(a=(())): 
#     z=[]
#     for j in range(0,len(a[0])):
#         u=[]
#         for i in range(0,len(a)):
#             u.append(a[i][j])
#         z.append(tuple(u))
#     return(z)

# print(unzip2(a))

print("Test1",list(unzip(list(zip((1,2,3,4), (5,6), (7,8))))) == [(1,2), (5,6), (7,8)])
t = [(1,2), (3,4), (5,6)]
print("Test2",list(unzip(list(unzip(t)))) == t)


