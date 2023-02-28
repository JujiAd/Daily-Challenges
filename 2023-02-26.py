"""
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""

def build_houses(matrix):
    n = len(matrix)
    k = len(matrix[0])
    solution_matrix = [[0]*k]

    #Solution matrix: matrix[i][j] represents the minimum cost to build house i with color j
    for r, row in enumerate(matrix):
        row_cost = []
        for c, val in enumerate(row):
            row_cost.append(min(solution_matrix[r][i] for i in range(k) if i != c) + val)

        solution_matrix.append(row_cost)
    return min(solution_matrix[-1])

# This runs in O(N*K^2) time and O(N*K) space

# We only ever look at the last row when computing the next row's cost. We only need to keep track of one array of size K instead of the whole N*K array.
def build_houses(matrix):
    k = len(matrix[0])
    sol_row = [0]*k
    for r, row in enumerate(matrix):
        new_row = []
        for c, val in enumerate(row):
            new_row.append(min(sol_row[i] for i in range(k) if i != c) + val)
        sol_row = new_row

    return min(sol_row)

# This runs in O(N*K^2) time and O(K) space 
"""
Hold on a second. When we're looking at the previous row's total cost, it looks like we're almost computing the same thing each time: the minimum of the previous row that isn't the current index.

For every element that isn't that index, it will be the same value. When it is that index, it will be the second-smallest value.

Now, armed with this insight, we only need to keep track of three variables:

The lowest cost of the current row
The index of the lowest cost
The second lowest cost
Then, when looking at the value at each row, we only need to do the following:

Check if the index is the index of the lowest cost of the previous row. If it is, then we can't use this color -- we'll use the second lowest cost instead. Otherwise, use the lowest cost of the previous row
Calculate the minimum cost if we painted this house this particular color
Update our new lowest cost/index or second lowest cost if appropriate
Now we'll always have our lowest cost in a variable, and once we've gone through the matrix we can just return that.
"""

from math import inf

def build_houses(matrix):
    lowest_cost, lowest_cost_index = 0, -1
    second_lowest_cost = 0

    for r, row in enumerate(matrix):
        new_lowest_cost, new_lowest_cost_index = inf, -1
        new_second_lowest_cost = inf
        for c, val in enumerate(row):
            prev_lowest_cost = second_lowest_cost if c == lowest_cost_index else lowest_cost
            cost = prev_lowest_cost + val
            if cost < new_lowest_cost:
                new_second_lowest_cost = new_lowest_cost
                new_lowest_cost, new_lowest_cost_index = cost, c
            elif cost < new_second_lowest_cost:
                new_second_lowest_cost = cost
        lowest_cost = new_lowest_cost
        lowest_cost_index = new_lowest_cost_index
        second_lowest_cost = new_second_lowest_cost

    return lowest_cost

# Now the runtime is only O(N * K) and the space complexity is O(1) - constant, since we keep track of only three variables!