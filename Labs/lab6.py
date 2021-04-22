import random
# Warm Up

test_board = ['X', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O']
def print_board(board):
  print(board[0], board[1], board[2])
  print(board[3], board[4], board[5])
  print(board[6], board[7], board[8])
  

def open_spots(board):
  open = []
  for i in range(len(board)):
    if board[i] == '-':
      open.append(i)
  return open

# print_board(test_board)
# print(open_spots(test_board))

# Stretch
def random_move(board, symbol):
  move = random.choice(open_spots(board))
  board[move] = symbol
  return board

# print_board(random_move(test_board, 'O'))

# Work Out
def check_three(board, idx1, idx2, idx3):
  x1 = board[idx1]
  x2 = board[idx2]
  x3 = board[idx3]

  if (x1 == 'X') and (x2 == 'X') and (x3 == 'X'):
    return 'X'
  elif (x1 == 'O') and (x2 == 'O') and (x3 == 'O'):
    return 'O'
  else:
    return '-'

#print(check_three(['X', 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'O'],3,1,2))

def winner(board):
  combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
 
  for triple in combos:
    board_check = check_three(board, triple[0], triple[1], triple[2])
    if board_check == "X": return 'X'
    elif board_check == "O": return 'O'
    
  if open_spots(board) == []: return 'D'  
  else: return '-'

# print(winner(['X', 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'O']))
# print(winner(['X', '-', 'O', 'X', 'O', '-', 'O', '-', 'X']))
# print(winner(['O', 'X', 'O', 'X', 'X', 'O', 'X', 'O', 'X']))
# print(winner(['X', 'X', 'O', '-', 'X', '-', 'X', 'O', 'O']))
# print(winner(['-', '-', '-', 'X', 'X', 'X', 'O', 'O', '-']))


# Challenge

def tic_tac_toe():
  turns = ['X', 'O']
  turn_counter = 0
  new_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

  while (open_spots(new_board) != []) & (winner(new_board) == "-"):
    turn_symbol = turns[turn_counter % 2]
    new_board = random_move(new_board, turn_symbol)
    print_board(new_board)
    print()
    turn_counter += 1
  return winner(new_board)


def play_tic(total_runs):
  x_wins = 0
  o_wins = 0
  draws = 0
  for i in range(total_runs):
    game = tic_tac_toe()

    if game == 'X': x_wins += 1
    elif game == 'O': o_wins += 1
    elif game == 'D': draws += 1
  print("X Wins:", x_wins, "\nO Wins:", o_wins, "\nDraws:", draws)

play_tic(100)
