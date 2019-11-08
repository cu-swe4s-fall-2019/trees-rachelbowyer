import unittest
import random
import binary_tree as bt
import sys
sys.path.insert(1, "./avl_tree")
import avl


class TestTrees(unittest.TestCase):
    """tests of the insert_...pairs script"""

    def test_bt_inserts(self):
        """test if the binary tree insert works"""
        Tree = None
        Tree = bt.add(Tree, "keys", 10)
        self.assertNotEqual(Tree, None)

    def test_bt_searches(self):
        """test if the binary tree searchs works
        for a randomly chosen key/value pair
        """
        f = open("rand.txt", "r")
        lines = f.readlines()
        result = []
        for x in lines:
            result.append(x.rstrip().split('\t'))
        f.close()
        choice = random.choice(result)
        Tree = None
        Tree = bt.add(Tree, result[0], result[1])
        search = bt.search(Tree, result[0])
        self.assertEqual(search, result[1])

    def test_avl_inserts(self):
        """test if the avl tree insert works"""
        tree = avl.AVL()
        tree.insert(10)
        self.assertNotEqual(tree, None)

    def test_avl_searches(self):
        """test if the avl tree searchs works
        for a randomly chosen key/value pair
        """
        f = open("rand.txt", "r")
        lines = f.readlines()
        result = []
        for x in lines:
            result.append(x.rstrip().split('\t'))
        f.close()
        choice = random.choice(result)
        tree = avl.AVL()
        tree.insert(choice[1])
        g = tree.find(choice[1])
        self.assertNotEqual(g, choice[1])


if __name__ == '__main__':
    unittest.main()
