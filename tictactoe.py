#this is a simple tic tac toe game
from array import *

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

	if brd[rowCorrect][columnCorrect] == 4:
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
			print(movementROW)
			if movementROW == '1' or movementROW == '2' or movementROW == '3':
				inputROW = True
				print ('here')
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

		choice = boardCheck(boardREAL,movementROW,movementCOLUMN)
		if choice == False:
			print('Place already taken on board, re-enter a new one')
			movementCOLUMN = ''
			movementROW = ''

	#for adding movement to board
	boardREAL = boardMOVEMENT(boardREAL,movementROW,movementCOLUMN)
	funcl(boardREAL)

	# this if for clearing the inputs after sent to board
	movementCOLUMN = ''
	movementROW = ''
	inputROW = False
	inputColumn = False
	choice = False