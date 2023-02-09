# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:47:13 2023

@author: jadle
"""

"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

#Generate list of numbers
import random
nums = []
for i in range(0,10):
    n = random.randint(1,20)
    nums.append(n)
print(nums)

#nums = [10, 2, 7, 8, 18, 13, 15, 11, 5, 3]
#Solve that shit
k = 2
flag = False

for num1 in nums:
    for num2 in nums:
        if num1 + num2 == k:
            print(f'{num1} + {num2} = {k}')
            flag = True
    
if flag == False:
    print('Solution not found')