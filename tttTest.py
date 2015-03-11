"""
Name: Simon J. Bloch
Date: 3-7-2015
Program: Test File for tttPlayer and tttGame
"""
import tttPlayer
import tttGame


def main():
    p1 = tttPlayer.tttPlayer("AI")
    p2 = tttPlayer.tttPlayer("manual")

    game = tttGame.tttGame(p2,p1)
    game.playGame()


main()