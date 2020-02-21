#!/usr/bin/env python

# Adversarial Search using Minimax Algorithm.
# Created by Chance Cardona 2/19/2020

from math import inf

# returns [move, score] here move is column.
def minimax(currentGame, player, alpha, beta, depth):
    #Game has points, so not 0 sum.
    if player == 1:     #1 is MAX   -1 is MIN
        best = [-1, -inf]
    else:
        best = [-1, inf]

    if depth == 0 or currentGame.pieceCount == 42:
        currentGame.countScore()
        #TODO find a better Evaluation Function than current Score
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
        currentGame.playPiece(col)                                  #Execute move
        [move, score] = minimax(currentGame, -player, alpha, beta, depth - 1)    #Recur
        currentGame = prevGame                                      #Undo move
        if player == 1:
            if score > best[1]:
                best = [col, score]
            if score > alpha:
                alpha = score
        else:
            if score < best[1]:
                best = [col, score]
            if score < beta:
                beta = score
        if alpha >= beta:
            break

    return best
