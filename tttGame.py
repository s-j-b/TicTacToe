"""
Name: Simon J. Bloch
Date: 3-7-2015
Program: Class Description for Tic Tac Toe Game
"""

import tttPlayer


class tttGame(object):
    def __init__(self,p1,p2):
        self.gameboard = [" "," "," "," "," "," "," "," "," "]
    
        self.gameOrder = ["x","o","x","o","x","o","x","o","x"]

        self.p1 = p1
        
        self.p2 = p2

        self.turn = 0

    def setTurn(self):
        self.turn = 9-self.gameboard.count(" ")
    
    def getTurn(self):
        return turn

    def getToMove(self):
        return self.gameOrder[self.turn]

    def move(self):
        toGo = self.getToMove()



        if toGo == "x":
            #move is an index value of a board position
            move = self.p1.getMove(self.gameboard,"x")

        else:
            #move is an index value of a board position
            move = self.p2.getMove(self.gameboard,"o")
        
        
        self.gameboard[int(move)] = toGo
        
        #set the turn number
        self.setTurn()

    def drawBoard(self):
        gb = self.gameboard
        for i in range(3):
            print gb[3*i], "|", gb[3*i+1], "|", gb[3*i+2]
            if i!=2:
                print "_________"

    def playGame(self):
        dunzo = False
        i = 1
        while not dunzo:
            self.drawBoard()
            print
            print
            self.move()

        
            dunzo = self.isDone()

        if dunzo == [" "]:
            print "Tie Game"

        else:
            print dunzo[0], "Wins"

    def isDone(self):
        if self.turn == 9:
            return [" "]

        if self.hasWin("x"):
            return ["x"]

        if self.hasWin("o"):
            return ["o"]

        return []
            
    def hasWin(self,p):
        b = self.gameboard
    
        if b[0]==p and b[1]==p and b[2]==p:
            return True
        if b[3]==p and b[4]==p and b[5]==p:
            return True
        if b[6]==p and b[7]==p and b[8]==p:
            return True
        if b[0]==p and b[3]==p and b[6]==p:
            return True
        if b[1]==p and b[4]==p and b[7]==p:
            return True
        if b[2]==p and b[5]==p and b[8]==p:
            return True
        if b[0]==p and b[4]==p and b[8]==p:
            return True
        if b[2]==p and b[4]==p and b[6]==p:
            return True
        return False


    def reset(self):
        gameboard = [" "," "," "," "," "," "," "," "," "]
        
        turn = 0




