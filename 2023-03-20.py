"""
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""

# Super clever answer I found on geeksforgeeks, but runs in O(NlogN) and O(N)
def single_num(nums):

    return (3 * sum(set(nums)) - sum(nums)) / 2

if __name__ == "__main__":
    lst = [6, 1, 3, 3, 3, 6, 6]
    print(f'The clever solution returned {int(single_num(lst))}')


def getSingle(arr, n):
    ones = 0
    twos = 0
     
    for i in arr:
        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise XOR
        twos = twos ^ (ones & i)
        print(f'twos: {twos}')
         
        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise XOR
        ones = ones ^ i
        print(f'ones: {ones}')
         
        # The common bits are those bits
        # which appear third time. So these
        # bits should not be there in both
        # 'ones' and 'twos'. common_bit_mask
        # contains all these bits as 0, so
        # that the bits can be removed from
        # 'ones' and 'twos'
        common_bit_mask = ~(ones & twos)
         
        # Remove common bits (the bits that
        # appear third time) from 'ones'
        ones &= common_bit_mask
         
        # Remove common bits (the bits that
        # appear third time) from 'twos'
        twos &= common_bit_mask
    return ones
     
# driver code
arr = [6, 1, 3, 3, 3, 6, 6]
n = len(arr)
print("The element with single occurrence is ",
        getSingle(arr, n))


    