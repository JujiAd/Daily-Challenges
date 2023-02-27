# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 19:42:23 2023

@author: jadle
"""

"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

"""
The idea is to simulate random (x, y) points in a 2-D plane with domain as a square of side 2r units centered on (0,0). Imagine a circle inside the same domain with same radius r and inscribed into the square. We then calculate the ratio of number points that lie inside the circle and total number of generated points. 
https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/

A_circle = πr^2
A_square = (2r)^2

A_circle/A_square = π/4

For many points, π/4 = (No. points inside circle)/(Total No. of points)

1. Initialize circle_points, square_points and interval to 0. 
2. Generate random point x. 
3. Generate random point y. 
4. Calculate d = x*x + y*y. 
5. If d <= 1, increment circle_points. 
6. Increment square_points. 
7. Increment interval. 
8. If increment < NO_OF_ITERATIONS, repeat from 2. 
9. Calculate pi = 4*(circle_points/square_points). 
10. Terminate.
"""

import random

interval = 1000

circle_points = 0
square_points = 0

# Total random numbers generated = (possible x values)*(possible y values)
for i in range(interval**2):
    rand_x = random.uniform(-1,1)
    rand_y = random.uniform(-1,1)
    
    d = rand_x**2 + rand_y**2
    
    if d <= 1:
        circle_points += 1
    
    square_points += 1
        
    pi = 4*circle_points/square_points

print(pi)
