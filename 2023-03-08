# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:30:44 2023

@author: M35243
"""

"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""


s = "AAAABBBCCDAA"
y = "4A3B2C1D2A"

def encoder_decoder(s):
    
    if s[0].isalpha():
        
        new_s = ''
        current_count = 0
        
        current_char = ''
        
        for i, char in enumerate(s):
            if current_char == '':
                current_char = char
                
            if char == current_char:
                current_count += 1
                
            if char != current_char:
                new_s += str(current_count) + current_char
                current_count = 1
                current_char = char
                print(i)
                
            if i == len(s)-1:
                new_s += str(current_count) + current_char
                
    if not s[0].isalpha():
        
        new_s = ''
        for i, char in enumerate(s):
            if char.isalpha():
                new_s += char*int(s[i-1])
            

    return new_s
