"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""

# Using built in python methods
import statistics

lst = [2, 1, 5, 7, 2, 0, 5]

med_lst = []

for num in lst:
    med_lst.append(num)
    print(statistics.median(med_lst))

# Lets calculate the median ourselves
print('\n'*2)
med_lst = []

for num in lst:
    med_lst.append(num)
    med_lst.sort()

    if len(med_lst) % 2 == 0:
        i = int(len(med_lst)/2)
        print((med_lst[i]+med_lst[i-1])/2)
    
    elif len(med_lst) == 1:
        print(med_lst[0])
        
    elif len(med_lst) % 2 != 0 and len(med_lst) != 1:
        i = int((len(med_lst)-1)/2)
        print(med_lst[i])
