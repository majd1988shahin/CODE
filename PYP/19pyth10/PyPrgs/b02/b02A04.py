lis=[1,2,3]
lis.append(4)
print("Append",lis)
lis2=[5,6]

lis.extend(lis2)
print("extend",lis)

lis.insert(3,7)
print("insert",lis)

lis.remove(7)
print("remove",lis)

print("index of 5 is ",lis.index(5))

print("count of 2 is",lis.count(2))

lis.pop()
print("list after pop",lis)

lis.reverse()
print("list nach reverse",lis)

lis.sort()
print("list nach sort",lis)

a=lis.copy()
print("Ist Copy der Liste die selbe List ?",a is lis)

lis.clear()
print("List Nach clear",lis)

lis=[0,1, 2, 3, 4, 5]
print("List :",lis)

print("gibt es ein True element in der Liste ?",any(lis))

print("Sind alle Elemente True ?",all(lis))

otherText = 'Pythön is interesting'
print("Normal print :",otherText)
print("ascii print :",ascii(otherText))

print("List als bool :",bool(lis))


grocery = ['bread', 'milk', 'butter']

print('\n')
for count, item in enumerate(grocery):
  print(count, item)


alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels of the list :',alphabets,' are:')
for vowel in filteredVowels:
    print(vowel)
iterator =iter(lis)
print("nechstes Ding :",next(iterator))
print("nechstes Ding :",next(iterator))
print("nechstes Ding :",next(iterator))

#https://www.programiz.com/python-programming/methods/list

print("Converts all to list list() :",list(((1,2),3,(4,5,6))))

#print(locals())

print("Lange der Liste",lis," ist : ",len(lis))

print("Max ist :",max(lis))
print("Minimum ist :",min(lis))

sq=map(lambda x: x**2,lis)
print(sq)
print(set(sq))#geht auch mit list()  // tuple....
rev =reversed(lis)#returns reversed iterator of a sequence

print("reverced list: ",list(rev))

print("sorted list : ", list(sorted(reversed(lis))))
s=slice(0,3,2)
print("sliceObject :",s)
print("sliced list :",lis[s])
print("Summe der liste :",sum(lis))

print ("iterator von Tuples :",zip(lis))
print ("erste element next(zip(lis)) :",next(zip(lis)))