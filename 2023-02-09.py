# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:12:47 2023

@author: M35243
"""

"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

lst = [1, 2, 3, 4, 5]


#Generate list of numbers
import random
def rand_lst(list_length,list_range):
    
    lst = []
    for i in range(0,list_length):
        n = random.randint(1,list_range)
        lst.append(n)
    print(f'Randomly generated list: {lst}')
    return lst

def array_product(lst):
    answer = []
    product = 1
    for num in lst:
        product = product*num
    
    for i in range(len(lst)):
        answer.append(int(product/lst[i]))
    return answer
        

#What if I can't divide?
#Pop that SHIT

def array_product2(lst):
    answer = []
    for num in lst:

        product = 1
        temp_lst = lst.copy()
        temp_lst.pop(temp_lst.index(num))
        for num in temp_lst:
            product = product*num
        answer.append(product)
    return answer
            
def solver(list_length, list_range):
    lst = rand_lst(list_length, list_range)
    answer = array_product(lst)
    print(f'First method, with division: {answer}')            
    
    answer2 = array_product2(lst)
    print(f'Second method, without division: {answer2}') 
