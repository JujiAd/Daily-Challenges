"""
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""

# Create a node class

class node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def evaluateTree(root):
    # empty tree
    if root is None:
        return 0
    
    # If the node has no children, it must be a leaf
    if root.left is None and root.right is None:
        return int(root.data)
    
    # evaluate left tree
    leftSum = evaluateTree(root.left)

    # evaluate right tree
    rightSum = evaluateTree(root.right)

    # check which operation to apply
    if root.data == '+':
        return leftSum + rightSum
    if root.data == '-':
        return leftSum - rightSum
    if root.data == '*':
        return leftSum * rightSum
    if root.data == '/':
        return leftSum / rightSum
    
# Test code
if __name__ == '__main__':
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('-4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('20')

    print(evaluateTree(root))