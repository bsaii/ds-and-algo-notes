## Function to create a binary tree using tuple

The provided tuple is `tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))`

```
def parse_tuple(data):
    print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node
```

The `parse_tuple` creates a new root node when a tuple of size 3 as an the input. Interestingly, to create the left and right subtrees for the node, the `parse_tuple` function invokes itself. This technique is called _recursion_. The chain of _recursive_ calls ends when `parse_tuple` encounters a number or `None` as input. We'll use recursion extensively throughout this tutorial.

## Function to calculate the height/depth of a binary tree

```
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))
```

## Function to calculate the size of a binary tree (the number of nodes in a binary tree)

```
def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)
```

## Function to check if a binary tree is a binary search tree and return the min and max values

A binary search tree or BST is a binary tree that satisfies the following conditions:

1. The left subtree of any node only contains nodes with keys less than the node's key
2. The right subtree of any node only contains nodes with keys greater than the node's key

```
# Function to remove None from nums
def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    # condition to check if a binary tree is a binary search tree
    is_bst_node = (is_bst_l and is_bst_r and
              (max_l is None or node.key > max_l) and
              (min_r is None or node.key < min_r))

    # remove none from the min_key and max_key
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    # print(node.key, min_key, max_key, is_bst_node)

    return is_bst_node, min_key, max_key
```

## Function to create a balanced BST from a sorted list/array of key-value pairs

```
# Storing key-value pairs using BST
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)

    return root

```
