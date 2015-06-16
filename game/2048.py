from random import randint
import os
import time
import sys
import random
import getch
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



board = [[0 for x in range(4)] for x in range(4)] 
score=0

def init_board(board):
	x=randint(0,3)
	y=randint(0,3)
	board[x][y]=random.choice([2,4])
	x1=randint(0,3)
	y1=randint(0,3)
	if(x==x1 and y==y1):
		if(x1==3):
			x=0
		else:
			x1+=1
	board[x1][y1]=random.choice([2,4])
	
def disp_board(board):
	os.system('clear')
	global score
	print color.RED +color.BOLD + '__________________________________2048 Game___________________________________' + color.END
	print "Use w,a,s,d for up,left,down,right directions respectively \n"
	print "Enter n for new game\t\t\t\t Enter x to exit\n"
	print "\t\t\t\t\t Score = %d" %score
	for i in range(4):
		print "\t\t.     .     .     .     ."
		print "\t\t",		
		for j in range(4):
			
			if(board[i][j]==0):
				print "      ",
			else: 
				print " %d   " %board[i][j],
		print ""
	print "\t\t.     .     .     .     ."
		

def right(board):
	j=0
	global score
	for i in range(4):
		if board[i][j]!=0 or board[i][j+1]!=0 or board[i][j+2]!=0:
			while board[i][j+3]==0:
				board[i][j+3]=board[i][j+2]
				board[i][j+2]=board[i][j+1]
				board[i][j+1]=board[i][j]
				board[i][j]=0
				time.sleep(0.05)
				disp_board(board)
		if board[i][j]!=0 or board[i][j+1]!=0:
			while board[i][j+2]==0:
				board[i][j+2]=board[i][j+1]
				board[i][j+1]=board[i][j]
				board[i][j]=0	
				time.sleep(0.05)
				disp_board(board)
		if board[i][j]!=0:
			while board[i][j+1]==0:
				board[i][j+1]=2*board[i][j]
				board[i][j]=0
				time.sleep(0.05)
				disp_board(board)
		

	for i in range(4):
		if board[i][j+3]==board[i][j+2]:
			board[i][j+3]=2*board[i][j+3]
			score+=board[i][j+3]
			board[i][j+2]=board[i][j+1]
			board[i][j+1]=board[i][j]
			board[i][j]=0
		if board[i][j+2]==board[i][j+1]:
			board[i][j+2]=2*board[i][j+1]
			board[i][j+1]=board[i][j]
			board[i][j]=0
			score+=board[i][j+2]
		if board[i][j+1]==board[i][j]:
			board[i][j+1]=2*board[i][j]
			board[i][j]=0
			score+=board[i][j+1]

def left(board):
	j=0
	global score
	for i in range(4):
		if board[i][j+1]!=0 or board[i][j+2]!=0 or board[i][j+3]!=0:
			while board[i][j]==0:
				board[i][j]=board[i][j+1]
				board[i][j+1]=board[i][j+2]
				board[i][j+2]=board[i][j+3]
				board[i][j+3]=0
				time.sleep(0.05)
				disp_board(board)
		if board[i][j+2]!=0 or board[i][j+3]!=0:		
			while board[i][j+1]==0:
				board[i][j+1]=board[i][j+2]
				board[i][j+2]=board[i][j+3]
				board[i][j+3]=0
				time.sleep(0.05)
				disp_board(board)
		if board[i][j+3]!=0:
			while board[i][j+2]==0:
				board[i][j+2]=board[i][j+3]
				board[i][j+3]=0
				time.sleep(0.05)
				disp_board(board)
			
	for i in range(4):
		if board[i][j]==board[i][j+1]:
			board[i][j]=2*board[i][j+1]
			board[i][j+1]=board[i][j+2]
			board[i][j+2]=board[i][j+3]
			board[i][j+3]=0
			score+=board[i][j]
		if board[i][j+1]==board[i][j+2]:
			board[i][j+1]=2*board[i][j+2]
			board[i][j+2]=board[i][j+3]
			board[i][j+3]=0
			score+=board[i][j+1]
		if board[i][j+2]==board[i][j+3]:
			board[i][j+2]=2*board[i][j+3]
			board[i][j+3]=0
			score+=board[i][j+2]
			
def up(board):
	i=0
	global score
	for j in range(4):
		if board[i+1][j]!=0 or board[i+2][j]!=0 or board[i+3][j]!=0:
			while board[i][j]==0:
				board[i][j]=board[i+1][j]
				board[i+1][j]=board[i+2][j]
				board[i+2][j]=board[i+3][j]
				board[i+3][j]=0
				time.sleep(0.05)
				disp_board(board)
		if board[i+2][j]!=0 or board[i+3][j]!=0:		
			while board[i+1][j]==0:
				board[i+1][j]=board[i+2][j]
				board[i+2][j]=board[i+3][j]
				board[i+3][j]=0
				time.sleep(0.05)
				disp_board(board)
		if board[i+3][j]!=0:
			while board[i+2][j]==0:
				board[i+2][j]=board[i+3][j]
				board[i+3][j]=0
				time.sleep(0.05)
				disp_board(board)
	
			
	for j in range(4):
		if board[i][j]==board[i+1][j]:
			board[i][j]=2*board[i+1][j]
			board[i+1][j]=board[i+2][j]
			board[i+2][j]=board[i+3][j]
			board[i+3][j]=0
			score+=board[i][j]
		if board[i+1][j]==board[i+2][j]:
			board[i+1][j]=2*board[i+2][j]
			board[i+2][j]=board[i+3][j]
			board[i+3][j]=0
			score+=board[i+1][j]
		if board[i+2][j]==board[i+3][j]:
			board[i+2][j]=2*board[i+3][j]
			board[i+3][j]=0
			score+=board[i+2][j]
	
		
def down(board):
	i=0
	global score
	for j in range(4):
		if board[i][j]!=0 or board[i+1][j]!=0 or board[i+2][j]!=0:
			while board[i+3][j]==0:
				board[i+3][j]=board[i+2][j]
				board[i+2][j]=board[i+1][j]
				board[i+1][j]=board[i][j]
				board[i][j]=0
				time.sleep(0.05)
				disp_board(board)
		if board[i][j]!=0 or board[i+1][j]!=0:
			while board[i+2][j]==0:
				board[i+2][j]=board[i+1][j]
				board[i+1][j]=board[i][j]
				board[i][j]=0	
				time.sleep(0.05)
				disp_board(board)
		if board[i][j]!=0:
			while board[i+1][j]==0:
				board[i+1][j]=2*board[i][j]
				board[i][j]=0
				time.sleep(0.05)
				disp_board(board)
		
	
	for j in range(4):
		if board[i+3][j]==board[i+2][j]:
			board[i+3][j]=2*board[i+3][j]
			score+=board[i+3][j]
			board[i+2][j]=board[i+1][j]
			board[i+1][j]=board[i][j]
			board[i][j]=0
		if board[i+2][j]==board[i+1][j]:
			board[i+2][j]=2*board[i+1][j]
			board[i+1][j]=board[i][j]
			board[i][j]=0
			score+=board[i+2][j]
		if board[i+1][j]==board[i][j]:
			board[i+1][j]=2*board[i][j]
			board[i][j]=0
			score+=board[i+1][j]
init_board(board)
disp_board(board)
flag=1
while flag:
	move=raw_input()
	
	if move=='d':
		right(board)
	elif move=='a':
		left(board)
	elif move=='w':
		up(board)
	elif move=='s':
		down(board)
	elif move=='n':
		choice="a"
		while choice!="yes" and choice!="no":
			choice=raw_input("Are you sure ? (yes/no)  ->  ")
		
		if choice=="yes":
			board = [[0 for x in range(4)] for x in range(4)] 
			score=0
			init_board(board)
			disp_board(board)
			continue
		else:
			disp_board(board)
			continue
	elif move=='x':
		break
	else:
		disp_board(board)
		continue
	zero_row=[]
	zero_col=[]
	for i in range(4):
		for j in range(4):
			if board[i][j]==0:
				zero_row.append(i)
				zero_col.append(j)
			elif board[i][j]==2048:
				flag=0
				print "Congragulations!!! You made a 2048 tile"
				break

	if len(zero_row)>0:
		board[random.choice(zero_row)][random.choice(zero_col)]=random.choice([2,4])
	else:
		flag=0		
	disp_board(board)
print "You scored %d points" %score
