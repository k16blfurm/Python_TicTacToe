#this is a simple tic tac toe game
from array import *

def funcl(brd):
	tic = ("   a     b     c\n"                                                
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

def row1(column, brd):
	if column == 'a':
		brd[0][0] = 4
		return brd
	if column == 'b':
		brd[0][1] = 4
		return brd
	if column == 'c':
		brd[0][2] = 4
		return brd

def row2(column, brd):                                                     
		if column == 'a':                                                  
			brd[1][0] = 4                                              
			return brd                                                 
		if column == 'b':                                                  
			brd[1][1] = 4                                              
			return brd                                                 
		if column == 'c':                                                  
			brd[1][2] = 4                                              
			return brd

def row3(column, brd):                                                     
		if column == 'a':                                                  
			brd[2][0] = 4                                              
			return brd                                                 
		if column == 'b':                                                  
			brd[2][1] = 4                                              
			return brd                                                 
		if column == 'c':                                                  
			brd[2][2] = 4                                              
			return brd

def boardMOVEMENT(brd, ROW, COLUMN):
	if ROW == '1':
		print('here')
		x = row1(COLUMN, brd)
		return x
	if ROW == '2':
		y = row2(COLUMN, brd)
		return y
	if ROW == '3':
		z = row3(COLUMN, brd)
		return z

#this is the original board
boardREAL = [[0,0,0],[0,0,0],[0,0,0]]
#this is to show the user first time how to
#play the game
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

while gameOVER != True:
	print('enter a spot to place your piece/n')
	if(first == 1):
		print(guide)
		first = 0
	while(inputROW == False):
		#this is for filtering bad inputs
		movementROW = input()
		if movementROW == '1' or '2' or '3':
			inputROW = True
		if(inputROW == False):
			print('re-enter a correct value')
			movementROW = ''

	print('now enter your column')

	while(inputColumn == False):
		movementCOLUMN = input()
		if movementCOLUMN == 'a' or 'b' or 'c':
			inputColumn =  True
		if(inputColumn == False):
			print('re-enter a correct value')
			movementCOLUMN = ''

	#for adding movement to board
	boardREAL = boardMOVEMENT(boardREAL,movementROW,movementCOLUMN)
	funcl(boardREAL)

	# this if for clearing the inputs after sent to board
	movementCOLUMN = ''
	movementROW = ''