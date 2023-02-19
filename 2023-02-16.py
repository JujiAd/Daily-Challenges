# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:25:49 2023

@author: jadle
"""

"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
lst = [2, 4, 6, 2, 5]

def largest_non_adj(lst):
    if not lst:
        return 0
    
    return max(largest_non_adj(lst[1:]), lst[0] + largest_non_adj(lst[2:]))
        
# Calls itself recursively twice, not memory efficient

def largest_non_adjacent(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    cache = [0 for i in arr]
    cache[0] = max(0, arr[0])
    cache[1] = max(cache[0], arr[1])

    for i in range(2, len(arr)):
        num = arr[i]
        cache[i] = max(num + cache[i - 2], cache[i - 1])
    return cache[-1]

# Notice that this function only ever evaluates the last two values in the array. We can take advantage of that.

def largest_non_adjacent(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    max_excluding_last= max(0, arr[0])
    max_including_last = max(max_excluding_last, arr[1])

    for num in arr[2:]:
        prev_max_including_last = max_including_last

        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last

    return max(max_including_last, max_excluding_last)