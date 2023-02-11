# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:10:23 2023

@author: jadle
"""

"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def serialize(node):
    val = node.val
    if node.left:
        left = serialize(node.left)
    else:
        left = None
    if node.right:
        right = serialize(node.right)
    else:
        right = None
    serialized = [val, left, right]
    return serialized

def deserialize(serialized_node):
    val = serialized_node[0]
    if serialized_node[1]:
        left = deserialize(serialized_node[1])
    else:
        left = None
    if serialized_node[2]:
        right = deserialize(serialized_node[2])
    else:
        right = None
    return Node(val, left, right)

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val=="left.left"