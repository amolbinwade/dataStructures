# Problem Statement : Construct BST from given preorder traversal
# Given preorder traversal of a binary search tree, construct the BST.
# For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be root of following tree.
# This algo has time complexity of O(n^2)


class Node:

    def __init__(self):
        value = None
        left = None
        right = None

