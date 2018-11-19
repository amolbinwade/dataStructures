
# Problem Statement : Construct BST from given preorder traversal
# Given preorder traversal of a binary search tree, construct the BST.
# For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be root of following tree.
# This algo has time complexity of o(n (log n)^2)


class BST:

    # Steps to create BST:
    # 1. Create Root
    # 2. Create Left tree
    # 3. Create Right tree

    class Node:

        def __init__(self):
            self.value = None
            self.right = None
            self.left = None
            self.parent = None

    def __init__(self, elements, order):
        self.root = None
        self.preorder_index = 0
        if len(elements) < 1:
            raise Exception("Tree Error. No elements provided.")
        if order == None or order != "preorder":
            raise Exception("Tree Error. Order not specified.")
        if order == "preorder":
             self.create_preorder_bst(elements)


    def create_preorder_bst(self, elements):
        #create root
        for num in range(0, len(elements)):
            if num == 0:
                node = self.Node()
                node.value = elements[num]
                node.parent = None
                self.root = node
                print("root" + str(self.root.value))

            # decide left
            elif node.value > elements[num]:
                left_node = self.Node()
                left_node.value = elements[num]
                left_node.parent = node
                node.left = left_node
                node = left_node
                print("left node " + str(node.value))

            # decide right
            # if value > than current node and node's parent not null and parent's value is < than value
            # then traverse upward
            # if above traversed node is already having right node then traverse downwards
            elif node.value < elements[num]:
                while (node.value < elements[num]
                       and node.parent is not None
                       and node.parent.value < elements[num]):
                    node = node.parent
                    print("traverse upward. " + str(node.value))
                while node.right is not None:
                    node = node.right
                    print("traverse downward. " + str(node.value))
                right_node = self.Node()
                right_node.value = elements[num]
                right_node.parent = node
                node.right = right_node
                node = right_node
                print("right node " + str(node.value))

    def print_inorder(self, node):
        if node.left is not None:
            self.print_inorder(node.left)
        print(node.value)
        if node.right is not None:
            self.print_inorder(node.right)


elmentsT = [10, 5, 1, 7, 40, 50]
bst = BST(elmentsT, "preorder")
print(bst.root.value)
bst.print_inorder(bst.root)
