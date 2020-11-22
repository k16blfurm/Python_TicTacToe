#this is a simple tic tac toe game
from array import *
import random

def funcl(brd):
	tic = ( "   a     b     c\n"                                                
			"      |     |     \n"                                                     
			"1  %d  |  %d  |  %d  \n"                                                     
			" _____|_____|_____\n"                                                     
			"      |     |     \n"                                                     
			"2  %d  |  %d  |  %d  \n"                                                     
			" _____|_____|_____\n"                                                     
			"      |     |     \n"                                                     
			"3  %d  |  %d  |  %d  \n"                                                     
			"      |     |     \n"  
%(brd[0][0],brd[0][1],brd[0][2],brd[1][0],brd[1][1],brd[1][2],brd[2][0],brd[2][1],brd[2][2]))
	print(tic)

def calcScore(brd):
	if (brd[0][0] == 1 and brd[0][1] == 1 and brd[0][2] == 1):
		return 2
	if (brd[1][0] == 1 and brd[1][1] == 1 and brd[1][2] == 1):
		return 2
	if (brd[2][0] == 1 and brd[2][1] == 1 and brd[2][2] == 1):
		return 2
	if (brd[0][0] == 1 and brd[1][0] == 1 and brd[2][0] == 1):
		return 2
	if (brd[0][1] == 1 and brd[1][1] == 1 and brd[2][1] == 1):
		return 2
	if (brd[0][2] == 1 and brd[1][2] == 1 and brd[2][2] == 1):
		return 2
	if (brd[0][0] == 1 and brd[1][1] == 1 and brd[2][2] == 1):
		return 2
	if (brd[0][2] == 1 and brd[1][1] == 1 and brd[2][0] == 1):
		return 2
	if (brd[0][0] == 4 and brd[0][1] == 4 and brd[0][2] == 4):
		return 1
	if (brd[1][0] == 4 and brd[1][1] == 4 and brd[1][2] == 4):
		return 1
	if (brd[2][0] == 4 and brd[2][1] == 4 and brd[2][2] == 4):
		return 1
	if (brd[0][0] == 4 and brd[1][0] == 4 and brd[2][0] == 4):
		return 1
	if (brd[0][1] == 4 and brd[1][1] == 4 and brd[2][1] == 4):
		return 1
	if (brd[0][2] == 4 and brd[1][2] == 4 and brd[2][2] == 4):
		return 1
	if (brd[0][0] == 4 and brd[1][1] == 4 and brd[2][2] == 4):
		return 1
	if (brd[0][2] == 4 and brd[1][1] == 4 and brd[2][0] == 4):
		return 1
	else:
		return 0

def newGAME():
	boardNEW = [[0,0,0],[0,0,0],[0,0,0]]

def boardMOVEMENT(brd, ROW, COLUMN):
	if(ROW == '1'):
		if COLUMN == 'a':
			brd[0][0] = 4
		if COLUMN == 'b':
			brd[0][1] = 4
		if COLUMN == 'c':
			brd[0][2] = 4
	if(ROW == '2'):
		if COLUMN == 'a':
			brd[1][0] = 4
		if COLUMN == 'b':
			brd[1][1] = 4
		if COLUMN == 'c':
			brd[1][2] = 4
	if(ROW == '3'):
		if COLUMN == 'a':
			brd[2][0] = 4
		if COLUMN == 'b':
			brd[2][1] = 4
		if COLUMN == 'c':
			brd[2][2] = 4
	return brd

def boardMOVEMENTCPU(brd, ROW, COLUMN):
	if(ROW == '1'):
		if COLUMN == 'a':
			brd[0][0] = 1
		if COLUMN == 'b':
			brd[0][1] = 1
		if COLUMN == 'c':
			brd[0][2] = 1
	if(ROW == '2'):
		if COLUMN == 'a':
			brd[1][0] = 1
		if COLUMN == 'b':
			brd[1][1] = 1
		if COLUMN == 'c':
			brd[1][2] = 1
	if(ROW == '3'):
		if COLUMN == 'a':
			brd[2][0] = 1
		if COLUMN == 'b':
			brd[2][1] = 1
		if COLUMN == 'c':
			brd[2][2] = 1
	return brd

def boardCheckanyMoves(brd):

	for row in brd:
		for elem in row:
			if elem == 0:
				return True
	return False
				
		

def boardCheck(brd, ROW, COLUMN):
	if ROW == '1':
		rowCorrect = 0
	if ROW == '2':
		rowCorrect = 1
	if ROW == '3':
		rowCorrect = 2

	if COLUMN == 'a':
		columnCorrect = 0
	if COLUMN == 'b':
		columnCorrect = 1
	if COLUMN == 'c':
		columnCorrect = 2	

	if brd[rowCorrect][columnCorrect] == 4 or brd[rowCorrect][columnCorrect]  == 1:
		return False
	else:
		return True


#this is the original board
boardREAL = [[0,0,0],[0,0,0],[0,0,0]]
first = 1
guide = 'enter, for example "3", then enter "a"'
s = 'Welcome to my tic tac toe game\n'
str(s)
print(s)
gameOVER = False
funcl(boardREAL)
#this is for filtering bad inputs
inputROW = False
inputColumn = False
#this is for making sure that board piece isn't taken
choice = False
CPUmove = False
CheckMoves = True

while gameOVER != True:

	while(choice == False):
		print('enter a spot to place your piece')
		if(first == 1):
			print('computers choices are in 1s')
			print(guide)
			first = 0

		while(inputROW == False):
			#this is for filtering bad inputs
			movementROW = input()
			if movementROW == '1' or movementROW == '2' or movementROW == '3':
				inputROW = True
			if(inputROW == False):
				print('re-enter a correct value')
				movementROW = ''

		print('now enter your column')

		while(inputColumn == False):
			movementCOLUMN = input()
			if movementCOLUMN == 'a' or movementCOLUMN == 'b' or movementCOLUMN == 'c':
				inputColumn =  True
			if(inputColumn == False):
				print('re-enter a correct value')
				movementCOLUMN = ''

		# this is to check if the place on the board isn't already taken
		choice = boardCheck(boardREAL,movementROW,movementCOLUMN)
		if choice == False:
			print('Place already taken on board, re-enter a new one')
			movementCOLUMN = ''
			movementROW = ''
			inputColumn = False
			inputROW = False


	#copying the players choice to the array
	boardREAL = boardMOVEMENT(boardREAL,movementROW,movementCOLUMN)
	CheckMoves = boardCheckanyMoves(boardREAL)

	#checking if player won
	score = calcScore(boardREAL)
	if score == 1:
		print('Congrats, you won!!!')
		break
	if score == 2:
		print('Sorry, but the CPU Won')
		break
		


	if CheckMoves == False:	
		gameOVER = True


	# the cpu making it's move
	while(CPUmove == False and gameOVER != True):
		ColumnChoices = ['a', 'b', 'c']
		RowChoices = ['1', '2', '3']
		CPUcolumn = random.choice(ColumnChoices)
		CPUrow = random.choice(RowChoices)

		CheckMoves = boardCheckanyMoves(boardREAL)
		if CheckMoves == False:
			gameOVER == True

		CPUmove = boardCheck(boardREAL, CPUrow, CPUcolumn)
		if (CPUmove == False):
			CPUcolumn = ''
			CPUrow = ''

	#for adding movement to board for bot
	if gameOVER != True:
		boardREAL = boardMOVEMENTCPU(boardREAL, CPUrow, CPUcolumn)
	funcl(boardREAL)

	if gameOVER == True:
		print('calculating score')
		score = calcScore(boardREAL)
		if score == 0:
			print('Nobody Won, Try again')
		if score == 1:
			print('Congrats, you won!!!')
		if score == 2:
			print('Sorry, but the CPU Won')
		break

	#checking if CPU won
	score = calcScore(boardREAL)
	if score == 1:
		print('Congrats, you won!!!')
		break
	if score == 2:
		print('Sorry, but the CPU Won')
		break



	# this if for clearing the inputs after sent to board
	movementCOLUMN = ''
	movementROW = ''
	inputROW = False
	inputColumn = False
	choice = False
	CPUmove = False