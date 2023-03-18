"""
You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""
import time

# print the board
def print_board(board, n):
	for i in range(n):
		for j in range(n):
			print(board[i][j], end = " ")
		print()

# joining '.' and 'Q'
# making combined 2D Array
#For output in desired format
def add_sol(board, ans, n):
	temp = []
	for i in range(n):
		string = ""
		for j in range(n):
			string += board[i][j]
		temp.append(string)
	ans.append(temp)
	
	
# we need to check in three directions
# 1. in the same column above the current position
# 2. in the left top diagonal from the given cell
# 3. in the right top diagonal from the given cell
def is_safe(row, col, board, n):
	x = row
	y = col
	#check for same upper col
	while(x>=0):
		if board[x][y] == "Q":
			return False
		else:
			x -= 1
			
	#Check for Upper Right Diagonal
	x = row
	y = col
	while(y<n and x>=0):
		if board[x][y] == "Q":
			return False
		else:
			y += 1
			x -= 1
			
	#check for Upper Left diagonal
	x = row
	y = col
	while(y>=0 and x>=0):
		if board[x][y] == "Q":
			return False
		else:
			x -= 1
			y -= 1
	return True


# function to solve n queens
# solveNQueens function here will fill the queens
# 1. there can be only one queen in one row
# 2. if we filled the final row in the board then row will
# be equal to total number of rows in board
# 3. push that board configuration in answer set because
# there will be more than one answers for filling the board
# with n-queens
def solveNQueens(row, ans, board, n):
	#base Case
	#Queen is depicted by "Q"
	# adding solution to final answer array
	if row == n:
		add_sol(board, ans, n)
		return
	
	#solve 1 case and rest recursion will follow
	for col in range(n):
		# for each position check if it is safe and if it
		# is safe make a recursive call with
		# row+1, board[i][j]='Q' and then revert the change
		# in board that is make the board[i][j]='.' again to
		# generate more solutions
		if is_safe(row, col, board, n):
			# if placing Queen is safe
			board[row][col] = "Q"
			solveNQueens(row+1, ans, board, n)
			# Backtrack
			board[row][col] = "."
			


# Driver Code
if __name__ == "__main__":
	# size 4x4 is taken and we can pass some other
	# dimension for chess board as well
	n = 8
	
	# 2D array of string will make our board
	# which is initially all empty
	board = [["." for i in range(n)] for j in range(n)]
	# store all the possible answers
	ans = []
	start = time.time()
	
	solveNQueens(0, ans, board, n)
	end = time.time()
	time_taken = end - start
	
	if ans == []:
		print("Solution does not exist")
	else:
		print(len(ans))
		print(f"{time_taken:.06f} time was taken(in miliseconds)")
		print(f"Out Of {len(ans)} solutions one is following")
		print_board(ans[0], n)
		
	# This code is contributed by Priyank Namdeo
		

