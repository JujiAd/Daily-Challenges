# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:03:49 2023

@author: jadle
"""
"""
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element