board = []
for i in range(5):
    board.append(["O"] * 5)

print(board)


# creates list with 5 lists in it, each containing 5 elemts set to 0
# for index 0 create list of '0' times five

def print_board(board_in):
    """
        prints rows of board pretty as strings
        board is [ [0,0,0,0,0] , [0,0,0,0,0] .....]
        row is first iterable index of the board
        join joins all elements of the row (the list at index 0, 1, 2...
        puts a space between and makes it a string
    """
    for row in board:
        print(" ".join(row))  # joins all elements of rows in board to a list with ' ' between them to print pretty


print_board(board)

# to store the ships location I need 2 vars - one for the row two for the place in the row
# 1 - list 1 of rows (row), 2 - list to in row (column)
# lets create a fun to rand select nums of rows an col

from random import randint


def random_row(board_in):
    return randint(0, len(board_in) - 1)


def random_col(board_in):
    return randint(0, len(board_in) - 1)


# GUESSING GAME - ask the user to guess the place of the rand ship
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))



'''
from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
  print 'Turn', turn+1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    # if its turn4 exit game
    if turn == 3:
      print "Game Over"
    # Print (turn + 1) here!
    print_board(board)
'''

'''
Extra Credit
You can also add on to your Battleship! program to make it more complex and fun to play. Here are some ideas for enhancements—maybe you can think of some more!

Make multiple battleships: you’ll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You’ll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

Make your game a two-player game.

Use functions to allow your game to have more features like rematches, statistics and more!

Some of these options will be easier after we cover loops in the next lesson. Think about coming back to Battleship! after a few more lessons and see what other changes you can make!

Code Editor

'''