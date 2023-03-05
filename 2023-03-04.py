"""
Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
"""

import re

def finder(s,txt):

    x = re.search(s,txt)

    if len(x.group()) == len(txt):
        print('True')
        return True

    print('False')
    return False

print('First check: ra., raymond')
finder('ra.','raymond')
print('\n')

print('Second check: ra., ray')
finder('ra.','ray')
print('\n')

print('Third check: .*at, chat')
finder('.*at','chat')
print('\n')

print('Fourth check: .*at, chats')
finder('.*at','chats')
print('\n')

print('Fifth check: he.*o, hellllllo')
finder('he.*o','hellllllo') 
print('\n')