# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 11:50:15 2023

@author: jadle
"""

"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

#Generate list of numbers
import random
def rand_lst(list_length,list_range):
    
    lst = []
    for i in range(0,list_length):
        n = random.randint(-list_range,list_range)
        lst.append(n)
    print(f'Randomly generated list: {lst}')
    return lst

#This solution takes 0(N^2) time to solve and is not ideal. This solution iterates through all positive integers, starting at 1.
def first_int(list_length,list_range):
    
    lst = rand_lst(list_length,list_range)
    
    i = 1
    while i in lst:
        i += 1
    print(f'The first missing positive integer is {i}')
        

#The following solution takes O(N) time because it only iterates through both lists once.        
"""
Create a list full of 0’s with the size of the max value of the given array. 
Now, whenever we encounter any positive value in the original array, change the index value of the list to 1. 
After that simply iterate through the modified list, the first 0 encountered, (index value + 1) should be the answer.
"""

def solver(lst):
    
    m = max(lst) 
    
    #If all values are non-positive integers
    if m < 1:
        return 1
    #If lst is only 1 element long
    if len(lst) == 1:
        return 1
    
    #Make 0's list
    zero_lst = [0]*m
    
    #Change the index value of the 0's list to 1 if a positive integer is encountered
    for i in range(len(lst)):
        if lst[i] > 0:
            if zero_lst[lst[i]-1] != 1:
                zero_lst[lst[i]-1] = 1
    
    for i in range(len(zero_lst)):
        if zero_lst[i] == 0:
            return i + 1
    
    return i + 2


# Driver Code
if __name__ == '__main__':
    lst = rand_lst(10,5)
    print(solver(lst))