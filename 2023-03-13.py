"""
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""

def is_palindrome(s):
    return s == s[::-1]

def make_palindrome(s):
    # If s is a palindrome already, stop here and return s
    if is_palindrome(s):
        return s
    
    print(s)
    # If the first and last character of s match, move in one character and check again
    if s[0] == s[-1]:
        print(f's[0] = {s[0]}, s[-1] = {s[-1]}')
        return s[0] + make_palindrome(s[1:-1]) + s[-1]
    
    # If the inner and outer characters in s don't match, add characters until they do
    else:
        one = s[0] + make_palindrome(s[1:]) + s[0]
        two = s[-1] + make_palindrome(s[:-1]) + s[-1]
        print(s[0], one)
        print(s[-1], two)

        if len(one) < len(two):
            return one
        elif len(one) > len(two):
            return two
        else:
            return min(one,two)