from IPython.display import clear_output
import random
def display_board(board):
	clear_output()
	print(board[7]+'  !'+board[8]+'  !'+board[9])
	print('..!..!..')
	print(board[4]+'  !'+board[5]+'  !'+board[6])
	print('..!..!.')
	print(board[1]+'  !'+board[2]+'  !'+board[3])



def choose_marker():
	'''
	output will be in the form of tuple
	player1_marker,player2_marker=player_input()

	'''
	marker=''
	while not(marker=='x'or marker=='o'):
		marker=input(turn+ ' :Choose  x or o---->>')
	if marker=='x':
		return ('x','o')

	else:
		return('o','x')

	pass

def marker_position(board):
	position='n'
	while position not in [1,2,3,4,5,6,7,8,9]  or  not space_check(board,position):
		position=int(input('Enter the position 1-9-->'))
	return position


	
def place_marker(board,position,marker):
	board[position]=marker


def whose_first():
	flip=random.randint(0,1)
	if flip==0:
		return 'player1'
	else:
		return 'player2'

	# toss
	

def space_check(board,position):
	 board[position]=''


def win_check(board,marker):
	return ((board[7]==board[8]==board[9]==marker)
		or (board[4]==board[5]==board[6]==marker)
		or (board[1]==board[2]==board[3]==marker)
		or (board[7]==board[4]==board[1]==marker)
		or (board[8]==board[5]==board[2]==marker)
		or (board[7]==board[5]==board[3]==marker)
		or (board[1]==board[5]==board[9]==marker)
		)

def full_board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
	return True


def replay():
	choice= input("Do you Want to Play Again yes or no -->")
	return choice=='yes'
# Actual Game Start.....>>>>

print(' <<<<<Wel-Come>>>>')


board=['']*10
#player1_marker,player2_marker=choose_marker()
turn=whose_first()
print(turn +' Will play First')

play_game=input("Do You Want to play Game   y or n -->")
if play_game=='y':
	game_on=True
else:
	game_on=False

player1_marker,player2_marker = choose_marker()

print( player1_marker + "is  player 1 marker.. ")
print(player2_marker  + " iS player2 marker ..")

while game_on:

	if turn=='player1':
		display_board(board)
		position=marker_position(board)
		place_marker(board,position,player1_marker)
		#display_board(board)

		if win_check(board,player1_marker):
			display_board(board)
			print("Player 1 Won the Game ")
			game_on  = False
		else:
			if full_board_check(board):
				display_board(board)
				print("Match is Tie ")
				game_on=False
				break
				
			else:
				turn='player2'
	else:
		display_board(board)
		position=marker_position(board)
		place_marker(board,position,player2_marker)
		#display_board(board)

		if win_check(board,player2_marker):
			display_board(board)
			print("Player 2 Won the Game ")
			game_on=False
		else:
			if full_board_check(board):
				display_board(board)
				print("Match is Tie ")
				game_on=False
				
			else:
				turn='player1'
	if not replay():
		break


