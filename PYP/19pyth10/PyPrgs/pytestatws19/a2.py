#!/usr/bin/python3
"UndoList"

class UndoList(list):
    "UndoList, eine Liste in der eine (die letzte) Operation undobar ist"



def main_test():
    "einfache kleine Tests für Sie zum probieren und ändern"    
    ul = UndoList([1,2,3,4,5])
    print("orig ", ul)
    ul.append(6)
    print("after", ul)
    ul.undo()
    print("undo ", ul)
    


if __name__ == '__main__':
    main_test()

