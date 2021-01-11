# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:08:12 2020

@author: Karen Tan

"""
"""
Write the code for two-player Tic-Tac-Toe game
"""
import random

#Determine who go first
def chooseFirst():
    turn = random.choice(['X' , 'O'])
    print("The player who hold {0} go first!".format(turn))
    return turn

def displayBoard(board):
    print(board[0],"|",board[1],"|",board[2])
    print('----------')
    print(board[3],"|",board[4],"|",board[5])
    print('----------')
    print(board[6],"|",board[7],"|",board[8], "\n")

#Simulate a player place a piece on the board
def placePiece(emptySquares, turn):
    location = random.choice(emptySquares)
    board[location] = turn
    emptySquares.remove(location)

#Check whether there is a winner
def hasWinner(board):
    for item in waysToWin:
        if board[item[0]] == board[item[1]] == board[item[2]] != ' ':
            winner = board[item[0]]
            return winner
    if ' ' not in board:
        return 'draw'
    else:
        return None

def nextTurn(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'

#The winning combination    
waysToWin = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

#Set player1 get X piece, palyer2 get O piece
player = {'X' : 'palyer1' , 'O' : 'player2'}
#Determine who go first
turn = chooseFirst()

#Define the board
board = [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ']
#Record all empty squares
emptySquares = list(range(9))
displayBoard(board)

#Simulate the game
while not hasWinner(board):
    print("Next is {0} who hold {1} move.".format(player[turn], turn))
    placePiece(emptySquares, turn)
    displayBoard(board)
    turn = nextTurn(turn)
else:
    winner = hasWinner(board)
if winner == 'draw':
    print("This is a draw game.")
else:
    print(player[winner], "win the game.")    



