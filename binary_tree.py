#                      2
#                     / \
#                    3    5
#                   /   /   \
#                  1    3     7
#                       \     /\
#                        4   6  8


class NodeTree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def add_node(self, data):
        if self.key == data:
            return

        elif data < self.key:
            if self.left:
                self.left.add_node(data)
            else:
                self.left = NodeTree(data)
        else:
            if self.right:
                self.right.add_node(data)
            else:
                self.right = NodeTree(data)

    def __str__(self) -> str:
        return str(self.key)


# def build_tree(element):
#     root = NodeTree(element[0])
#     for i in element[1:]:
#         root.add_node(i)
#     return root


# element = [17, 2, 5, 12, 6, 56, 18, 20, 25]


root = NodeTree(17)
node0 = NodeTree(2)
node1 = NodeTree(5)
node2 = NodeTree(18)
node3 = NodeTree(20)
node4 = NodeTree(3)
node5 = NodeTree(1)


root.left = node1
root.left.left = node0
root.left.left.left = node5
# root.left.left.left.left = node4


root.right = node2
root.right.right = node3


def inorder_traversal(tree):
    if tree is None:
        return []
    return inorder_traversal(tree.left) + [tree.key] + inorder_traversal(tree.right)


print(inorder_traversal(root))


def maxHeight(root):
    if root is None:
        return 0
    return 1 + max(maxHeight(root.left), maxHeight(root.right))


# print(maxHeight(root))


def treeSize(root):
    if root is None:
        return 0
    return 1 + treeSize(root.left) + treeSize(root.right)


# print(treeSize(root))


def max_value(tree):
    if tree is None:
        return 0

    left_max = max_value(tree.left)
    right_max = max_value(tree.right)
    value = 0

    if left_max > right_max:
        value = left_max
    elif right_max > left_max:
        value = right_max
    elif tree.key > value:
        value = tree.key

    return value


# print(max_value(root))


def min_value(tree):
    if tree is None:
        return float("inf")

    left_min = min_value(tree.left)
    right_min = min_value(tree.right)
    value = float("inf")

    if left_min > right_min:
        value = right_min
    elif right_min > left_min:
        value = left_min
    elif tree.key < value:
        value = tree.key

    return value


# print(min_value(root))

# 1) tree is binary search or not


def isBst(root, maxValue, minValue):

    if root is None:
        return True

    if root.key > maxValue or root.key < minValue:
        return False

    return isBst(root.left, root.key - 1, minValue) and isBst(
        root.right, maxValue, root.key - 1
    )


# print(isBst(root, max_value(root), min_value(root)))
# print(inorder_traversal(root))


# 2 ) check if tree is balance or not


def isBalance(node):

    if node is None:
        return True

    lh = maxHeight(node.left)
    rh = maxHeight(node.right)
    print(lh, rh)
    if (
        abs(lh - rh) <= 1
        and isBalance(node.left) is True
        and isBalance(node.right) is True
    ):
        return True
    return False


# print(isBalance(root))

# print(inorder_traversal(root))


