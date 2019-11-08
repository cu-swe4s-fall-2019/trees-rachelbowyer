class Node:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def add(root, key, value=None):
    if root is None:
        root = Node(key, value=value)
        return root
    else:
        if key < root.key:
            if root.left is None:
                root.left = Node(key, value=value)
            else:
                add(root.left, key, value=value)
        else:
            if root.right is None:
                root.right = Node(key, value=value)
            else:
                add(root.right, key, value=value)
        return root


def search(root, key):
    if root is None:
        # print('key not found')
        return root

    elif root.key is key:
        # print('value is '+str(root.value))
        return root.value

    # Key is greater than root's key
    elif root.key < key:
        # print('searching right')
        return search(root.right, key)

    # Key is smaller than root's key
    else:
        # print('searching left')
        return search(root.left, key)
        # return None
