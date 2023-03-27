"""
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""

def is_palindrome(s):
    if len(s) > 1:
        return s == s[::-1]

s = 'banana'
b = "aabcdcb"

# Runs in O(N^2)
def findPalindrome(s):

    # Check to see if s is a palindrome
    if is_palindrome(s):
        return s

    longestPalindrome = ''
   
    for i in range(len(s)):
        for j in range(len(s)+1):
            tempS = s[i:j]
            if is_palindrome(tempS):
                if len(tempS) > len(longestPalindrome):
                    longestPalindrome = tempS
                
    
    print(f'Answer: {longestPalindrome}')
    

findPalindrome(b)
