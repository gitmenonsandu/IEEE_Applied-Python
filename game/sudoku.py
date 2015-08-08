from random import randint
from sys import exit
import os
import time
board = [[0 for x in range(4)] for x in range(4)] 


def checkbox(board,x,m,n):

	if((m==1 or m==0)and(n==1 or n==0)):
		for i in range(0,2):
			for j in range(0,2):
				if(board[i][j]==x):
					return 0
		return 1
	elif((m==1 or m==0)and(n==3 or n==2)):
		for i in range(0,2):
			for j in range(2,4):
				if(board[m][j]==x):
					return 0
		return 1
	
	elif((m==2 or m==3)and(n==0 or n==1)):
		for i in range(2,4):
			for j in range(0,2):
				if(board[i][j]==x):
					return 0
		return 1

	elif((m==2 or m==3)and(n==2 or n==3)):
		for i in range(2,4):
			for j in range(2,4):
				if(board[i][j]==x):
					return 0
		return 1

def checkrow(board,x,m,n):
	for j in range(0,4):
		if(board[m][j]==x):
			return 0
	return 1

	
def checkcol(board,x,m,n):
	for i in range(0,4):
		if(board[i][n]==x):
			return 0
	return 1
		
	
def initboard(board):
	for i in range(0,4):
		for j in range(0,4):
			board[i][j]=0
	x=randint(1,4)
	board[0][0]=x
	y=randint(1,3)
	if(x!=4):
		x=x+1
		board[0][y]=x
	else:
		x=1
		board[0][y]=x
	for i in range(0,4):
		if(board[0][i]==0):
			if(x!=4):
				x=x+1
				board[0][i]=x
			else:
				x=1
				board[0][i]=x
	
	for i in range(1,4):
		x=1
		count=0
		while x<5:
			z=0
			for j in range(0,4):
				if(z==1):
					j=0
					z=0
				
				if(count>13):
					for k in range(0,4):
						board[i][k]=0
					x=1;
					count=0
					j=j+randint(1,3)
					if(j>3):
						j=0
						j=randint(0,3)
						
				if(board[i][j]==0):
					count=count+1
					b=checkcol(board,x,i,j)
					c=checkrow(board,x,i,j)
					if(b==1 and c==1):
						a=checkbox(board,x,i,j)
			
						if(a==1 and b==1 and c==1):
							board[i][j]=x
							x=x+1
							z=1
							count=0
							
				
def dispboard(board):
		
		for i in range(4):
			print board[i]
			
def setboard(board):
	for i in range(4):
		x=randint(0,3)
		y=randint(0,3)
		board[i][x]=0
		board[i][y]=0
		
initboard(board)
setboard(board)
dispboard(board)



def iffin(board):
	for i in range(4):
		for j in range(4):
			if(board[i][j]==0):
				return 1
				
	return 0

count=0
t=0
while iffin(board)==1:
	print "\n______________________________________________________"
	print "\n                    SUDOKU                            "
	print "\n______________________________________________________"
	print "\n\n The below table is a sudoku puzzle\n The boxes with zeroes are the one's to be filled\n Firts enter the row and column number (1-4) \n Then enter the value to be inserted into the sudoku board"
	print "let us begin..........."
	dispboard(board)
	r=input("Row      ->  ")
	c=input("Column   ->  ")
	
	if(board[r-1][c-1]!=0):
		count=count+1
		print "Sorry you cannot change that square.  Enter a square marked 0"
		t=2
		if(count%3==0):
			print " Do you want to quit \n 1 for yes\n 0 for no "
			p=input()
			if(p==0):
				count=-1
				break
	else:
		val=input("Value  ->  ")
		if(checkbox(board,val,r-1,c-1) and checkcol(board,val,r-1,c-1) and checkrow(board,val,r-1,c-1)):
			board[r-1][c-1]=val
			t=0
			count=0
		else:
			print "Sorry! That value does not belong there"
			count=count+1
			t=2
			if(count%3==0):
				print " Do you want to quit \n 1 for yes\n 0 for no "
				p=input()
				if(p==0):
					count=-1
					break
			
	time.sleep(t)
	os.system('cls')
	

if(count==-1):
	print "It's okay... \n Try again next time"
else:
	print "Congragulations!!!! You have solved the puzle"