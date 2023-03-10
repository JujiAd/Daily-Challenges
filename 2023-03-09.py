"""
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
"""
import random
import time

def water_volume(lst,n):
    startTime = time.time()
    volume = 0

    for i in range(1, n - 1):

        lw = lst[i]
        for j in range(i):
            lw = max(lw, lst[j])

        rw = lst[i]
        for j in range(i+1, n):
            rw = max(rw, lst[j])

        volume = volume +  min(lw, rw) - lst[i]

    executionTime = time.time() - startTime
    print(f'O(N^2) function execution time for n = 10000: {executionTime} s')
    return volume

if __name__ == "__main__":
    lst = []
    n = 10000
    for i in range(n):
        lst.append(random.randint(0,10))

    print(water_volume(lst,n))

# O(N^2) time, O(1) space

def maxWater(arr, n):
    startTime = time.time()
    size = n - 1
  
    prev = arr[0]
  
    prev_index = 0
    water = 0
  
    temp = 0
    for i in range(1, n):
        if arr[i] >= prev:
            prev = arr[i]
            prev_index = i
            temp = 0

        else:
            water += prev - arr[i]
            temp += prev - arr[i]

    if prev_index < size:
        water -= temp
        prev = arr[size]

        for i in range(size, prev_index - 1, -1):
            if arr[i] >= prev:
                prev = arr[i]
            else:
                water += prev - arr[i]
  
    # Return the maximum water
    executionTime = time.time() - startTime
    print(f'O(N) function execution time for n = 10000: {executionTime} s')
    return water

if __name__ == "__main__":
    print(maxWater(lst, n))

# O(N) time O(1) space