import sys
import argparse
import binary_tree as bt
import random
sys.path.insert(1, "./avl_tree")
import avl
sys.path.insert(1, "./hash-tables-rachelbowyer")
import hash_tables as ht


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Specify parameters")
    parser.add_argument('file', type=str, help='specify file name')
    args = parser.parse_args()

    file = args.file

    f = open(file, "r")
    lines = f.readlines()
    result = []
    for x in lines:
        result.append(x.rstrip().split('\t'))
    f.close()

    Tree = None

    for num in result:
        Tree = bt.add(Tree, num[0], value=num[1])

    for i in range(0, 10):
        choice = random.choice(result)  # choosing rand from file
        key = choice[0]  # extracting key
        val = bt.search(Tree, key)
