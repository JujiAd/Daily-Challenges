"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

def partition(arr):
    # Break the array into distinct chunks; [(:low)(low:mid)(mid:high)(high:)]. We don't know the indeces of low and mid yet, so set those to 0. Set high to len(arr)-1 so our initial 'unknown' section encompasses the entire array.
    # Strictly 'R's: array[:low]
    # Strictly 'G's: array[low:mid]
    # Unknown: array[mid:high]
    # Strictly 'B's: array[high:]
    low, mid, high = 0, 0, len(arr) - 1


    while mid <= high:
        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1