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
        score =  evalFunc(currentGame)
        return [-1, score]

    state = currentGame.gameBoard
    # Check how many pieces are in each col
    sumCol = [ sum( [1 for i in range(len(state)) if state[i][j]] ) for j in range(len(state[0])) ]
    notFull = (col for col in range(len(state[0])) if sumCol[col] < len(state))
    for col in notFull:
        currentGame.playPiece(col)                                                  #Execute move
        [move, score] = minimax(currentGame, -player, alpha, beta, depth - 1)       #Recur
        currentGame.undoPiece(col)                                                  #Undo move
        if player == 1:
            if score > best[1]:
                best = [col, score]
            if best[1] > alpha:
                alpha = best[1]
        else:
            if score < best[1]:
                best = [col, score]
            if best[1] < beta:
                beta = best[1]
        if alpha >= beta:
            break

    return best


def evalFunc(currentGame):
    currentGame.countScore()
    p1Score = currentGame.player1Score
    p2Score = currentGame.player2Score
    #p1OddThreat =
    #p2OddThreat =
    #p1EvenThreat =
    #p2EvenThreat =
    if currentGame.currentTurn == 1:
        return 1*p1Score - 1*p2Score
    else:
        return -1*p1Score + 1*p2Score
