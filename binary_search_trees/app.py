# the user class and it displays all the user infromation
class User:
    def __init__(self, username, name, email) -> str:
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self) -> str:
        return self.__repr__()


# Testing the function above
# user1 = User('saiicodes', 'bernardsaii', 'bernardsaii@example.com')
# print(user1)


# Binary Tree

# creating a simple binary tree using numbers
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


node0 = TreeNode(3)  # the root node
node1 = TreeNode(4)  # the left node
node2 = TreeNode(5)  # the right node

# setting the left and right node
node0.left = node1
node0.right = node2

# calling the tree
# tree = node0
# print('root:', tree.key)
# print('left node:', tree.left.key)
# print('right node:', tree.right.key)


# making the code for writing a binary tree easy using tuples
tree_tuples = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

# function to turn a tuple to a binary tree


def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        # make the middle the root
        node = TreeNode(data[1])
        # make the left and right nodes using recursion
        node.left = parse_tuple(data[0])  # left node
        node.right = parse_tuple(data[2])  # right node

    # node is node
    elif data is None:
        node = None

    else:
        # when the data is only one
        node = TreeNode(data)
    return node


# print(parse_tuple(tree_tuples))
tree = parse_tuple(tree_tuples)

# inorder traversal(left, root, right)
# we create a binary tree using the parse_tree function and then traverse it in order


def traverse_in_order(node):
    if node is None:
        return []
    return (
        traverse_in_order(node.left) + [node.key] +
        traverse_in_order(node.right)
    )


# print('inorder traversal:', traverse_in_order(tree))


# preorder traversal(root, left, right)
def traverse_pre_order(node):
    if node is None:
        return []
    return (
        [node.key] + traverse_pre_order(node.left) +
        traverse_pre_order(node.left)
    )


# print('preorder traversal:', traverse_pre_order(tree))


# post order traversal(left, right, root)
def traverse_post_order(node):
    if node is None:
        return []
    return (traverse_post_order(node.left) + traverse_post_order(node.right) + [node.key])


### The height of a binary tree ###
def tree_height(tree):
    if tree is None:
        return 0
    return 1 + max(tree_height(tree.left), tree_height(tree.right))


# print('The height of the tree is:', tree_height(tree))


# The size of the tree
def tree_size(tree):
    if tree is None:
        return 0
    return 1 + tree_size(tree.left) + tree_size(tree.right)


#


### Binary Search Tree ###

# remove none from nums
def remove_none(nums):
    return [x for x in nums if x is not None]

# is bst


def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    # conditions
    is_bst_node = (
        is_bst_l and is_bst_r and
        (max_l is None or node.key > max_l) and
        (min_r is None or node.key < min_r)
    )  # returns boolean

    # remove none
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    return is_bst_node, min_key, max_key


print(is_bst(None))


### Storing key-value pairs in BSTNode ###

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)


def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value


def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)

    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)

    return balanced, height


### Balanced Binary Search Tree ###
def make_balanced_bst(data, low=0, high=None, parent=None):
    if high is None:
        high = len(data) - 1
    if low > high:
        return None

    mid = (low + high) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, low, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, high, root)

    return root
