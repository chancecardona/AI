#!/usr/bin/env python

# Adversarial Search using Minimax Algorithm.
# Created by Chance Cardona 2/19/2020
from math import inf

# returns [move, score] here move is column.
# state is currentGame.gameBoard
# player is currentGame.currentTurn
# depth is int value input
def minimax(currentGame, depth):
    #Game has points, so not 0 sum.    
    if player == MAX:
        best = [-1, -inf]
    else:
        best = [-1, inf]

    if depth == 0 or currentGame.pieceCount == 42:
        score = currentGame.countScore()
        return [-1, score]

    state = currentGame.gameBoard
    # Check how many pieces are in each col
    sumCol = [ sum( [1 for i in range(len(state)) if state[i][j]] ) for j in range(len(state[0])) ]
    notFull = (col for col in range(len(state[0])) if sumCol[col] < len(state))
    for col in notFull:
        

