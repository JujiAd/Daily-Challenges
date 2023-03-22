"""
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""

def subset_sum(arr, k):
    def recursion(arr, k, i):
        # Sum is zero means we have found a subset.
        if k == 0:
            return True

        # At the end of the arr if the sum > 0 then
        # this subset sum does not equal to sum.
        if i == len(arr):
            return False

        # In case the current arr element is greater than
        # the sum k only consider excluding the element.
        if arr[i] > k:
            return recursion(arr, k, i+1)
        # To generate all subsets we've to include and exclude
        # the element at each index.
        else:
            return recursion(arr, k-arr[i], i+1) or recursion(arr, k, i+1)

    return recursion(arr, k, 0)