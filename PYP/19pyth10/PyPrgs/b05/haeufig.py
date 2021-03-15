import text

fileName="A Midsummer Night’s dream.txt"
print("Die haeufigeste 25 Woerter in  sind:",fileName)
dic=text.count.count_words(fileName)

[print({k:dic[k]}) for k in list(dic.keys())[0:25]]

