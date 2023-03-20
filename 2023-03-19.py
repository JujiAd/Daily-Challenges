"""
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost  live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""

def check_neighbours(row,col,live_coords):
    living_neighbours = 0
    if [row-1,col] in live_coords:
        living_neighbours += 1
    if [row+1,col] in live_coords:
        living_neighbours += 1   
    if [row,col-1] in live_coords:
        living_neighbours += 1
    if [row,col-1] in live_coords:
        living_neighbours += 1
    if [row-1,col-1] in live_coords:
        living_neighbours += 1
    if [row-1,col+1] in live_coords:
        living_neighbours += 1
    if [row+1,col-1] in live_coords:
        living_neighbours += 1
    if [row+1,col+1] in live_coords:
        living_neighbours += 1
    return living_neighbours



def initialize_board(live_coords):
    rows = max([coords[0] for coords in live_coords])+1
    cols = max([coords[1] for coords in live_coords])+1

    board = [["." for i in range(cols)] for j in range(rows)]

    for cell in live_coords:
        board[cell[0]][cell[1]] = '*'
    
    return board

def update_board(live_coords):
    rows = max([coords[0] for coords in live_coords])+1
    cols = max([coords[1] for coords in live_coords])+1

    board = [["." for i in range(cols)] for j in range(rows)]

    for cell in live_coords:
        board[cell[0]][cell[1]] = '*'
    print(board)

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == '.':
                if check_neighbours(i, j, live_coords) == 3:
                    board[i][j] = '*'
                    live_coords.append([i,j])

            if board[i][j] == '*':
                if check_neighbours(i, j, live_coords) < 2:
                    board[i][j] = '.'
                    live_coords.pop(live_coords.index([i,j]))
                if check_neighbours(i, j, live_coords) > 3:
                    board[i][j] = '.'
                    live_coords.pop(live_coords.index([i,j]))
            
    return board, live_coords


def print_board(board):
    rows = max([coords[0] for coords in live_coords])+1
    cols = max([coords[1] for coords in live_coords])+1

    for i in range(rows):
        for j in range(cols):
            print(board[i][j], end = " ")
        print()


def Game_of_Life(live_coords,n):

    for i in range(n):

        print(f'Step: {str(i)}')
        board, live_coords = update_board(live_coords)
        print_board(board)
        print('\n')

if __name__ == "__main__":
    live_coords0 = [[0,0],[1,0],[1,1],[1,5],[2,5],[2,6]]
    Game_of_Life(live_coords0,3)

    
    

        