
de2en={"eins":"one",1:"one","zwei":"two",2:"two",3:"three","drei":"three"}

print(1," ist ",de2en[1])
print("drei ist ",de2en["drei"])

print("dictionary :",de2en)
c=de2en.copy()
print("Copy of dictionary ",c)
de2en.clear()
print("dictionary ist lear",de2en)


