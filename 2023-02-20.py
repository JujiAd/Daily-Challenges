# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 19:32:19 2023

@author: jadle
"""

"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def substring(s,k):
    
    start, end = 0, k
    max_len = k
    
    while end <= len(s):
        if len(set(s[start:end])) <= k:
            current_len = end - start
            if current_len >= max_len:
                max_len = current_len
                
            end += 1
        
        else:
            start += 1
            
    return max_len

"""
We can improve this by instead keeping a running window of our longest substring. We'll keep a dictionary that maps characters to the index of their last occurrence. Then, as we iterate over the string, we'll check the size of the dictionary. If it's larger than k, then it means our window is too big, so we have to pop the smallest item in the dictionary and recompute the bounds. If, when we add a character to the dictionary and it doesn't go over k, then we're safe -- the dictionary hasn't been filled up yet or it's a character we've seen before.
"""
def longest_substring_with_k_distinct_characters(s, k):
    if k == 0:
        return 0

    # Keep a running window
    bounds = (0, 0)
    h = {}
    max_length = 0
    for i, char in enumerate(s):
        h[char] = i
        if len(h) <= k:
            new_lower_bound = bounds[0] # lower bound remains the same
        else:
            # otherwise, pop last occurring char
            key_to_pop = min(h, key=h.get)
            new_lower_bound = h.pop(key_to_pop) + 1

        bounds = (new_lower_bound, bounds[1] + 1)
        max_length = max(max_length, bounds[1] - bounds[0])

    return max_length
        
"""
This takes O(n * k) time and O(k) space.
"""
