"""
Name: Simon J. Bloch
Date: 3-7-2015
Program: Class Description for Tic Tac Toe Player
"""

from copy import *

class tttPlayer(object):
    def __init__(self, type):
        self.type = type
        self.player = "x"
        self.opponent = "o"
    
    def setOpponent(self):
        self.opponent = "o"
        if self.player == "o":
            self.opponent = "x"

    def getMove(self,gameboard,p):
        self.player = p
        self.setOpponent()

        if self.type=="manual":
            return self.getMoveManual(p)
        
        if self.type=="AI":
            return self.getMoveAI(gameboard)
    

    def getMoveManual(self,p):
        move = raw_input("What is your move? ")
        return move

    def getMoveAI(self, gameboard):
        gb = gameboard[:]
        minval = -1000
        
        best = [0,minval]
        
        for i in range(9):
            if gb[i]==" ":
                
                rank = self.minrank(gb,i)
                
                if rank > best[1]:
                    best = [i,copy(rank)]
        return best[0]
            

    def minrank(self,gameboard,pos):

        
        gb = gameboard[:]
        maxval = 1000
        minval = -1000

        p = self.player
        o = self.opponent

        gb[pos] = p

        if self.hasWin(p,gb):
            return maxval
        if self.hasWin(o,gb):
            return minval
        if gb.count(" ")==0:
            return 0
        

        worst = maxval
    
        for i in range(9):
            if gb[i]==" ":
                rank = self.maxrank(gb,i)
                if rank < worst:
                    worst = copy(rank)
        return worst




    def maxrank(self,gameboard,pos):
        gb = gameboard[:]
        
        maxval = 1000
        minval = -1000
        
        p = self.player
        o = self.opponent


        gb[pos] = o
        

        if self.hasWin(p,gb):
            return maxval
        if self.hasWin(o,gb):
            return minval
        if gb.count(" ")==0:
            return 0

        best = minval

        for i in range(9):
    
            if gb[i]==" ":
                rank = self.minrank(gb,i)
                if rank > best:
                    best = copy(rank)
                
        return best


    def hasWin(self,p,b):
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