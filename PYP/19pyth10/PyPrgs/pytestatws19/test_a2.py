#!/usr/bin/python3
"Test UndoList"
import time
import unittest
import a2

class TestA2(unittest.TestCase):
    "Test der Klasse UndoList mit Ihren Methoden aus a2"

    def test_undolist_islist(self):
        # is a list
        lists  = [[1, 2, 3], ['a', 'b', 'c'], [5,4,5,4,5,4,3,21]]
        for lis in lists:
            self.assertEqual([e for e in a2.UndoList(lis)], lis)
        for lis in lists:            
            self.assertEqual(len(a2.UndoList(lis)), len(lis))
        # did not change
        self.assertEqual(lists, [[1,2, 3], ['a', 'b', 'c'], [5,4,5,4,5,4,3,21]])
        # did copy
        lis = [1, 2, 3]
        ul = a2.UndoList(lis)
        ul[0] = 17
        self.assertEqual(1, lis[0])
        lis = [1, 2, 3]
        ul = a2.UndoList(lis)
        lis[0] = 17
        self.assertEqual(1, ul[0])
        # and at least one undo
        ul = a2.UndoList([1,2])
        ul.append(3)
        self.assertEqual([1,2,3], ul)
        ul.undo()
        self.assertEqual([1,2], ul)        

    def test_undolist_simpleundos(self):
        ul = a2.UndoList([1,2,3,4,5])
        ul.append(6)
        self.assertEqual([1,2,3,4,5,6], ul)
        ul.undo()
        self.assertEqual([1,2,3,4,5], ul)
        ul = a2.UndoList([1,2,3,4,5])
        ul.extend([6,17,42])
        self.assertEqual([1,2,3,4,5,6,17,42], ul)
        ul.undo()
        self.assertEqual([1,2,3,4,5], ul)
        ul = a2.UndoList([1,2,3,4,5])
        ul.insert(0, 0)
        self.assertEqual([0,1,2,3,4,5], ul)
        ul.undo()
        self.assertEqual([1,2,3,4,5], ul)

    def test_undolist_simpleremainingundos(self):
        ul = a2.UndoList([1,2,3,4,5])
        del ul[3]
        self.assertEqual([1,2,3,5], ul)
        ul.undo()
        self.assertEqual([1,2,3,4,5], ul)
        ul = a2.UndoList([1,2,3,4,5])
        ul.remove(4)
        self.assertEqual([1,2,3,5], ul)
        ul.undo()
        self.assertEqual([1,2,3,4,5], ul)
        ul = a2.UndoList([1,2,3,4,5])
        ul[-1] = None
        self.assertEqual([1,2,3,4,None], ul)
        ul.undo()
        self.assertEqual([1,2,3,4,5], ul)


if __name__ == '__main__':
    unittest.main()
