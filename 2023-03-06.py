"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def is_balanced(s):

    lst = []

    for char in s:
        if char in ['[','(','{']:
            lst.append(char)
        if char in [']',')','}']:
            if char == ')' and lst[-1] == '(':
                lst.pop()
            if char == ']' and lst[-1] == '[':
                lst.pop()
            if char == '}' and lst[-1] == '{':
                lst.pop()
    
    if len(lst) == 0:
        print('String is balanced')
    else:
        print('String is not balanced')
