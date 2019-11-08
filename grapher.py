import sys
import argparse
import binary_tree as bt
import random
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt
sys.path.insert(1, "./avl_tree")
import avl
sys.path.insert(1, "./hash-tables-rachelbowyer")
import hash_tables as ht
import hash_functions as hf


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Specify parameters")
    parser.add_argument('file', type=str, help='specify file name')
    parser.add_argument('nonfile', type=str, help='file name of non keys')
    parser.add_argument('N', type=int, help='specify keys to search')
    args = parser.parse_args()

    file = args.file
    nonfile = args.nonfile
    N = args.N

    # opening an extracting file
    f = open(file, "r")
    lines = f.readlines()
    result = []
    for x in lines:
        result.append(x.rstrip().split('\t'))
    f.close()

    ff = open(nonfile, "r")
    lines = ff.readlines()
    non_result = []
    for x in lines:
        non_result.append(x.rstrip().split('\t'))
    ff.close()

    """
    ########## binary tree ##########
    """
    # initializing binary tree
    BT_tree = None
    for num in result:
        BT_tree = bt.add(BT_tree, num[0], value=num[1])

    """
    ########## AVL tree ##########
    """
    # initializing avl tree
    AVL_tree = avl.AVL()
    for num in result:
        AVL_tree.insert(num[1])

    """
    ########## hash table ##########
    """
    Table = ht.ChainedHash(10000, hf.h_rolling)
    for num in result:
        Table.add(num[0], num[1])

    """
    ########## benchmarking ##########
    """
    norm_time = np.zeros((3, len(range(0, N))))
    non_time = np.zeros((3, len(range(0, N))))
    insert_time = np.zeros((3, len(range(0, N))))

    for i in range(0, N):
        # searching benchmarking
        choice = random.choice(result)  # choosing rand from file
        key = choice[0]  # extracting key

        non_choice = random.choice(non_result)  # choosing rand from file
        non_key = non_choice[0]  # extracting key

        t1 = time.time()
        for j in range(0, i):
            val = bt.search(BT_tree, key)
        t2 = time.time()
        for j in range(0, i):
            val = bt.search(BT_tree, non_key)

        t3 = time.time()
        for j in range(0, i):
            AVL_tree.find(choice[1])
        t4 = time.time()
        for j in range(0, i):
            AVL_tree.find(non_choice[1])

        t5 = time.time()
        for j in range(0, i):
            Table.search(key)
        t6 = time.time()
        for j in range(0, i):
            Table.search(non_key)
        t7 = time.time()

        norm_time[0, i] = t2 - t1
        norm_time[1, i] = t4 - t3
        norm_time[2, i] = t6 - t5

        non_time[0, i] = t3 - t2
        non_time[1, i] = t5 - t4
        non_time[2, i] = t7 - t6

        # inserting benchmarking
        sub_result = result[0:i]  # subsampling results

        sub_BT_tree = None
        sub_AVL_tree = avl.AVL()
        sub_Table = ht.ChainedHash(i+1, hf.h_rolling)

        t00 = time.time()
        for num in sub_result:
            sub_BT_tree = bt.add(BT_tree, num[0], value=num[1])
        t11 = time.time()
        for num in sub_result:
            sub_AVL_tree.insert(num[1])
        t22 = time.time()
        for num in sub_result:
            sub_Table.add(num[0], num[1])
        t33 = time.time()

        insert_time[0, i] = t11 - t00
        insert_time[1, i] = t22 - t11
        insert_time[2, i] = t33 - t22

fig = plt.figure()
plt.plot(range(0, N), norm_time[0], label="Binary Tree")
plt.plot(range(0, N), norm_time[1], label="AVL Tree")
plt.plot(range(0, N), norm_time[2], label="Hash Table")
plt.title("Time Taken Searching For Keys")
plt.xlabel('Number of Keys Searched For')
plt.ylabel('Time in seconds')
plt.legend()

plt.savefig('Search_' + file[:-4] + '.jpg', bbox_inches="tight")

fig = plt.figure()
plt.plot(range(0, N), non_time[0], label="Binary Tree")
plt.plot(range(0, N), non_time[1], label="AVL Tree")
plt.plot(range(0, N), non_time[2], label="Hash Table")
plt.title("Time Taken Searching for Keys NOT There")
plt.xlabel('Number of Keys Search')
plt.ylabel('Time in seconds')
plt.legend()

plt.savefig('Search_Not_There_' + file[:-4] + '.jpg', bbox_inches="tight")

fig = plt.figure()
plt.plot(range(0, N), insert_time[0], label="Binary Tree")
plt.plot(range(0, N), insert_time[1], label="AVL Tree")
plt.plot(range(0, N), insert_time[2], label="Hash Table")
plt.title("Keys Inserted vs Time")
plt.xlabel('Number of Keys Inserted')
plt.ylabel('Time in seconds')
plt.legend()

plt.savefig('Insert_Time_' + file[:-4] + '.jpg', bbox_inches="tight")
