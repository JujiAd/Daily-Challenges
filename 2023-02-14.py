# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:52:38 2023

@author: jadle
"""

"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def num_encodings(code):
    if code.startswith('0'):
        return 0
    elif len(code) <= 1:
        return 1
    
    total = 0
    
    if int(code[:2]) <= 26:
        total += num_encodings(code[2:])
        
    total += num_encodings(code[1:])
    
    return total

# Not very efficient because it calls itself recursively twice

from collections import defaultdict

def encoder(code):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    cache[len(code)] = 1 # Empty string is 1 valid encoding
    
    for i in reversed(range(len(code))):
        if code[i].startswith('0'):
            cache[i] = 0;
        elif i == len(code) == 1:
            cache[i] = 1
        else:
            if int(code[i:i+2]) <= 26:
                cache[i] = cache[i+2]
            cache[i] =+ cache[i+1]
    
    return cache[0]