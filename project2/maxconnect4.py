#!/usr/bin/env python

# Originally written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
#
# Modified by Chance Cardona
# Written to be Python 3.7 compatible since we don't live in 2008

import sys
from MaxConnect4Game import *

def oneMoveGame(currentGame, depth):
    #print('Game state before move:')
    #currentGame.printGameBoard()
    #currentGame.countScore()
    #print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if currentGame.pieceCount == 42:    # Is the board full already?
        print('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    currentGame.aiPlay(depth) # Make a move (only random is implemented)

    #Print Score and State
    print('Game state after move:')
    currentGame.printGameBoard()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    #Save Board State
    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame, nextTurn, depth):
    while currentGame.pieceCount < 42:    # Keep going until board is full
        #print('Game state before move:')
        #currentGame.printGameBoard()
        #currentGame.countScore()
        #print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

        if nextTurn == 'human-next':
            #Human Plays
            currentGame.humanPlay()
            #Save Board State
            currentGame.gameFile = open('human.txt', 'w')
            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()
            nextTurn = 'computer-next'
        elif nextTurn == 'computer-next':
            #AI plays
            currentGame.aiPlay(depth)
            #Save Board State
            currentGame.gameFile = open('computer.txt', 'w')
            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()
            nextTurn = 'human-next'

        print('Game state after move:')
        currentGame.printGameBoard()
        currentGame.countScore()
        print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    print('BOARD FULL\n\nGame Over!\n')
    sys.exit(0)


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]
    depth = int(argv[4])


    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print('\nMaxConnect-4 game\n')
    print('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        nextTurn = argv[3]
        if not nextTurn == 'computer-next' and not nextTurn == 'human-next':
            print('%s is an unrecognized next player. Please enter either computer-next or human-next' % nextTurn)
            sys.exit(2)
        interactiveGame(currentGame, nextTurn, depth) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame, depth) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)



