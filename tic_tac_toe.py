anything = None
board = [0,1,2,3,4,5,6,7,8]
def draw_board(board):

  print()
  print(board[0], '|', board[1], '|', board[2])
  print('----------')
  print(board[3], '|', board[4], '|', board[5])
  print('----------')
  print(board[6], '|', board[7], '|', board[8])
  print()

def make_move(player, where):
  print()
  board[where] = player
  draw_board(board)
  if not check_win(player, board,wincombos):
    next_Player = other_player(player)
    if anything != None and anything != player:
      next_move = bot_move(board, anything)
      print("AI: " + str(next_move))
    else:
      next_move = ask_move(next_Player)

    make_move(next_Player, next_move)

def ask_move(player):
  while True:
    try:
      move = input("Player" + player + ":")
      move = int(move)
      if move > -1 and move <9:
        temp_var = board[move]
        if temp_var != 'X' and temp_var != 'O':
          return move
      print ("Hey remember you should try to move somewhere that\nis actually on the board")
    except:
      print("Invalid move")

wincombos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
def check_win(player, board, wincombos):


  for i in wincombos:
    if board[i[0]] == board[i[1]] == board[ i[2] ] == player:
      print ('Player ' + player + ' is superior at tic tac toe... the other player\nshould go to daycare to learn basic strategy again!\n')
      return True
  count = 0
  for i in list(range(len(board))):
    if type(board[i]) == int:
      count += 1
  if count == 0:
    print ('You have shown the tic tac toe gods\nthat neither of you are worthy!')
    return True
  return False

def other_player(player):
  if player == 'X':
    return 'O'
  else:
    return 'X'

def availiable_moves(board):
  moves = []
  for i in range(9):
    if board[i] != 'X' and board[i] != 'O':
      moves.append(i)
  return moves

bob=0

def tic_tac_toe():
  global anything
  global bob
  print("Hello step right up, step right up,\ntest your luck at TIC-TAC-TOE!\nIf you win you will get your prize!\nJust kidding, there is no prize, I'm broke")
  bob = input("\n\nAlso, do you want to play against a bot? You look kind of lonely.\n").lower().strip()
  if bob == "yes" or bob == "y":
    anything = 'O'
    move = bot_move(board,anything)
    make_move(anything, move )
    anything = 'O'

  draw_board(board)
  make_move('X', ask_move('X'))


wincombos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


import random

def bot_move(board, player):
  wincombos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  random.randint(0, 8)
  x = availiable_moves(board)
  print(x)
  index = random.randint(0, len(x)-1)
  for i in range(len(wincombos)):
    vari_dummy = wincombos[i]
    dummy = [board[vari_dummy[0]], board[vari_dummy[1]], board[vari_dummy[2]]]
    if dummy.count('X')==2 and not dummy.count('O')==1:
      dummy.remove('X')
      dummy.remove('X')
      return dummy[0]
  for i in range(len(wincombos)):
    vari_dummy = wincombos[i]
    dummy = [board[vari_dummy[0]], board[vari_dummy[1]], board[vari_dummy[2]]]
    if dummy.count('O')==2 and not dummy.count('X')==1:
      dummy.remove('O')
      dummy.remove('O')
      return dummy[0]


  corner = [0, 2, 6, 8]
  why = availiable_moves(board)
  for i in corner:
    if i in why:
      return i
  return x[index]



tic_tac_toe()
