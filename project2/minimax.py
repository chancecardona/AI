#!/usr/bin/env python

# Adversarial Search using Minimax Algorithm.
# Created by Chance Cardona 2/19/2020
from math import inf
from copy import deepcopy
# returns [move, score] here move is column.
# state is currentGame.gameBoard
# player is currentGame.currentTurn
# depth is int value input
def minimax(currentGame, player, depth):
    #Game has points, so not 0 sum.
    if player == 1:     #1 is MAX   -1 is MIN
        best = [-1, -inf]
    else:
        best = [-1, inf]

    if depth == 0 or currentGame.pieceCount == 42:
        #print("TERMINAL NODE")
        currentGame.countScore()
        if currentGame.currentTurn == 1:
            score = currentGame.player1Score
        else:
            score = currentGame.player2Score
        return [-1, score]

    state = currentGame.gameBoard
    # Check how many pieces are in each col
    sumCol = [ sum( [1 for i in range(len(state)) if state[i][j]] ) for j in range(len(state[0])) ]
    notFull = (col for col in range(len(state[0])) if sumCol[col] < len(state))
    for col in notFull:
        prevGame = currentGame.fullCopy()
        #print("B4", currentGame.pieceCount, depth)
        currentGame.playPiece(col) #Execute move
        #if depth == 10:
        #print("Current Game at Depth and col", depth, col)
        #currentGame.printGameBoard()
        #print("Prev Game:")
        #prevGame.printGameBoard()
        [move, score] = minimax(currentGame, -player, depth - 1) #Recur
        currentGame = prevGame #Undo move
    #    print("After", currentGame.pieceCount, depth)
        if player == 1:
            if score > best[1]:
                best = [col, score]
                #print("New Best Score! Col", col, "Depth", depth)
                #currentGame.printGameBoard()
        else:
            if score < best[1]:
                best = [col, score]

    #print("Minimax is Returning!!! Depth", depth)
    #currentGame.printGameBoard()
    return best
