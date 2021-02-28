board = []
for i in range(5):
  board.append(["O"] * 5) # creates list with 5 lists in it, each containing 5 elemts set to 0


def print_board(board_in):
  '''prints rows of board pretty as strings'''
  for row in board:
    print(" ".join(row)) # joins all elements of rows in board to a list with ' ' between them to print pretty

print_board(board)