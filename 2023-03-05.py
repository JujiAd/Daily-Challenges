"""
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

def lst_pop(lst,k):
    
    popped_pos = len(lst)-k
    lst.pop(popped_pos)
    print(lst)