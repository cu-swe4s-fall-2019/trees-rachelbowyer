import sys
import argparse
import binary_tree as bt
import random
import time
sys.path.insert(1, "./avl_tree")
import avl
sys.path.insert(1, "./hash-tables-rachelbowyer")
import hash_tables as ht
import hash_functions as hf


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Specify parameters")
    parser.add_argument('file', type=str, help='specify file name')
    parser.add_argument('struc', type=str, help='specify data structure type')
    parser.add_argument('N', type=int, help='how many key/val pairs to use')
    
    args = parser.parse_args()

    file = args.file

    # opening an extracting file
    f = open(file, "r")
    lines = f.readlines()
    result = []
    for x in lines:
        result.append(x.rstrip().split('\t'))
    f.close()
    
    if args.N <= 10000:
        result = result[0:args.N] #subsampling results
    else:
        raise ValueError

    """
    ########## binary tree ##########
    """
    if args.struc == 'tree':
        # initializing binary tree
        Tree = None

        t0 = time.time()
        for num in result:
            Tree = bt.add(Tree, num[0], value=num[1])

        t1 = time.time()
        for i in range(0, 100):
            choice = random.choice(result)  # choosing rand from file
            key = choice[0]  # extracting key
            val = bt.search(Tree, key)

        t2 = time.time()

        print('Insertion time ' + str(t1-t0))
        print('Search time ' + str(t2-t1))

    """
    ########## AVL tree ##########
    """
    if args.struc == 'AVL':
        # initializing avl tree
        tree = avl.AVL()
        # print(tree)

        t3 = time.time()
        for num in result:
            tree.insert(num[1])
            # print()
            # print(tree)

        t4 = time.time()
        print("Insert time " + str(t4-t3))

        t5 = time.time()
        for i in range(0, 100):
            choice = random.choice(result)  # choosing rand from file
            g = tree.find(choice[1])

        t6 = time.time()

        print("Search time " + str(t6-t5))

    """
    ########## hash table ##########
    """
    if args.struc == 'hash':

        Table = ht.ChainedHash(10000, hf.h_rolling)

        t7 = time.time()

        for num in result:
            Table.add(num[0], num[1])

        t8 = time.time()

        print("Insert time " + str(t8-t7))

        t9 = time.time()

        for i in range(0, 100):
            choice = random.choice(result)
            Table.search(choice[0])

        t10 = time.time()

        print("Search time " + str(t10-t9))

    else:
        raise ValueError
