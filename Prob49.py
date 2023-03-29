"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

# Naive solution, runs in O(N^2)

lst = [34, -50, 42, 14, -5, 86]

maxSum = 0
for i in range(len(lst)):
    for j in range(len(lst)+1):
        if i <= j:
            maxSum = max(maxSum,sum(lst[i:j]))

print(maxSum)

# Dynamic programming solution

def maxSum(array):

    maxSumUsingElement = [array[0]]
    maxSum = array[0]

    for i in range(1, len(array)):
        num = array[i]
        currentMax = max(num, num + maxSumUsingElement[i-1])
        maxSumUsingElement.append(currentMax)
        maxSum = max(maxSum, currentMax)
    
    return maxSum

maxSum(lst)
