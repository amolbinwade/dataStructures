# Problem Statement : Construct BST from given preorder traversal
# Given preorder traversal of a binary search tree, construct the BST.
# For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be root of following tree.
# This algo has time complexity of O(n^2)


class Node:

    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def construct_pre_tree(low, high, lst):

        node = Node(lst[low], None, None)

        if high-low <= 3:
            if lst[low+1] > lst[low]:
                node.right = Node(lst[low+1], None, None)
                if (low+2) < len(lst):
                    node.left = Node(lst[low+2], None, None)
            if lst[low+1] < lst[low]:
                node.left = Node(lst[low+1], None, None)
                if (low+2) < len(lst):
                    node.right = Node(lst[low+2], None, None)
            return node

        for index in range(low, high+1):
            if lst[low] < lst[index]:
                node.left = construct_pre_tree(low+1, index-1, lst)
                if high > index:
                    node.right = construct_pre_tree(index, high, lst)
                return node


def construct(lst):
        low = 0
        high = len(lst)
        return construct_pre_tree(low, high, lst)


def print_inorder(node):
    if node.left is not None:
        print_inorder(node.left)
    print(node.value)
    if node.right is not None:
        print_inorder(node.right)


elmentsT = [10, 5, 1, 7, 40, 50]
root = construct(elmentsT)
print_inorder(root)