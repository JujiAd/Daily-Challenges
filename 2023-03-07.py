"""
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

#s = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16

def character_count(lst):
    return sum(len(i) for i in lst)


def justify(s,k):
    current_line = []
    
    for word in s:
        if character_count(current_line) + len(word) > k:
            if current_line[-1] == ' ':
                current_line.pop()

            i = 0
            while character_count(current_line) != k:
                    if current_line[i].isalpha() and current_line[i] != current_line[-1]:
                        current_line.insert(i+1,' ')
                    i += 1
                    if i == len(current_line):
                        i = 0
            
            print(current_line)
            print(character_count(current_line))

            current_line = []
            current_line.append(word)
            if character_count(current_line) < k:
                current_line.append(' ')
        
        else:
            current_line.append(word)
            if character_count(current_line) < k:
                current_line.append(' ')

        if word == s[-1] and character_count(current_line) < k:
            if current_line[-1] == ' ':
                current_line.pop()
            
            if len(current_line) == 1:
                while character_count(current_line) != k:
                    current_line.append(' ')
                    break
            
            i = 0
            while character_count(current_line) != k:
                if current_line[i].isalpha() and current_line[i] != current_line[-1]:
                    current_line.insert(i+1,' ')
                i += 1
                if i == len(current_line):
                    i = 0
    
    print(current_line)
    print(character_count(current_line))




