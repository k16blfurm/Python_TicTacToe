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

def a1():
	return 

def boardMOVEMENT(brd):
	hello= 9	


boardREAL = [[0,0,0],[0,0,0],[0,0,0]]
first = 1
guide = 'enter, for example "a1" or "c3"'
s = 'Welcome to my tic tac toe game\n'
str(s)
print(s)
gameOVER = False
funcl(boardREAL)


while gameOVER != True:
	print('enter a spot to place your piece/n')
	if(first == 1):
		print(guide)
		first = 0
	movement = input()
	print('now enter your column')
	#for adding movement to board
	boardREAL = boardMOVEMENT(boardREAL)
	funcl(boardREAL)
