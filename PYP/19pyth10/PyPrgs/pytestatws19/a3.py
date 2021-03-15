#!/usr/bin/python3
"Generatoren ites und secondonly"

def ith(gen):
    "jedes ite Vorkommen für i = 1, 2, 3, 4, 5..."
    pass

def secondonly(gen):
    "Nur jedes zweite Vorkommen"
    pass

def r(fro=1, to=100):
    "unendliche Sequenz von (Pseudo-)Zufallszahlen, bei jedem Aufruf gleich"
    import random
    random.seed(4217)
    while True:
        yield random.randint(fro, to)


def test_main():
    "einfache Tests, dürfen Sie ändern"
    lis = [1, 2, 3, 4, 5, 6]
    print(list(ith((e for e in lis))))
    lis = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 3, 5, 4, 2, 5, 1, 3, 2, 4]
    print(list(secondonly((e for e in lis))))
    gen = secondonly(r()) # unendliche Generatoren
    ele, lis = None, []
    while ele != 42: # finde die zweite 42
        ele = next(gen)
        lis.append(ele)
    pos = len(lis) # die wievielte Zahl war die zweite 42
    print(pos, lis[:3], lis[-3:])

if __name__ == '__main__':
    test_main()
