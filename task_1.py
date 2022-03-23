n = 8
black = 0
white = 1
squares = (black, white)

board = [[squares[(i+j) % 2] for i in range(n)] for j in range(n)]
print(board)
