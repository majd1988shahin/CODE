def count_chars(fileName):
    f=filter(lambda c :str.isalpha(c),open(fileName).read())
    u=map(lambda c: str.upper(c),f)
    dic=dict()
    for c in u:
        if c in dic:
            dic[c]=dic[c]+1
        else:
            dic[c]=1
    result=sorted(dic.items(),key=lambda kv: kv[1],reverse=True)
    return dict(result)

def count_words(fileName):
    f=open(fileName).read().lower().split()
    dic=dict()
    for W in f:
        if W in dic:
            dic[W]=dic[W]+1
        else:
            dic[W]=1
    result=sorted(dic.items(),key=lambda kv: kv[1],reverse=True)
    return dict(result)


print("count Module ist da!")