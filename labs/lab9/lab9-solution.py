from copy import deepcopy as copy
import numpy as np

class linkedlist():
    def __init__(self, board):
        self.val = copy(board)
        self.child = None
        self.jumpfrom = None
        self.jumpto = None
        
class board:
    def __init__(self, row_of_hole, col_of_hole):
        self.size = 5
        self.HolePos = [row_of_hole, col_of_hole]
        # 1 is peg. 0 is hole.
        self.board = [[1 for j in range(i+1)] for i in range(self.size)]
        self.board[row_of_hole][col_of_hole] = 0
        # direction: left, right, lefttop, righttop, bottomleft, bottomright
        self.newrow = [0,0,-2,-2,2,2]
        self.newcol = [-2,2,-2,0,0,2]
        self.midrow = [0,0,-1,-1,1,1]
        self.midcol = [-1,1,-1,0,0,1]
        self.start = linkedlist(self.board)
        self.current = self.start
            
    def drawBoard(self, board):
        for i in range(self.size):
            for j in range(self.size-i-1):
                print '',
            for j in board[i]:
                if j == 1:
                    print '+',
                else:
                    print 'o',
            print 
        
    def success(self):
        tmp = sum([sum(i) for i in self.board])
        if tmp==1:
            return True
        return False
    
    def printSolution(self):
        if self.success():
            self.current = self.start
            while self.current.child:
                self.drawBoard(self.current.val)
                print self.current.jumpfrom, "to ", self.current.jumpto
                self.current = self.current.child
            self.drawBoard(self.current.val)
        else:
            print "No solution has been found yet!"
    
    def isSafe(self, row, col, newrow, newcol, midrow, midcol, k):    
        ### newcol<=row+self.newrow[k] for top and bottom rows
        ## if newrow>=0 and newrow<self.size and newcol>=0 and newcol<=row+self.newrow[k] and \
        # another way
        if newrow>=0 and newrow<self.size and newcol>=0 and newcol<len(self.board[newrow]) and \
            self.board[newrow][newcol]==0 and self.board[midrow][midcol]==1:
            return True
        else:
            return False
        
    def solve(self):
        if self.success():
            return True
        
        for row in range(self.size):
            for col in range(len(self.board[row])):
                if self.board[row][col]:
                    for k in range(6):
                        newrow, newcol = row + self.newrow[k], col + self.newcol[k]
                        midrow, midcol = row + self.midrow[k], col + self.midcol[k]
                        if self.isSafe(row,col,newrow,newcol,midrow,midcol,k):
                            
                            self.board[midrow][midcol] = 0
                            self.board[row][col] = 0
                            self.board[newrow][newcol] = 1

                            parent = self.current
                            self.current = linkedlist(self.board)
                            parent.child, parent.jumpfrom, parent.jumpto = self.current, [row, col], [newrow, newcol]
                            
                            ## use this line to put the last peg in the position of the initial hole
                            #if self.solve() and self.board[self.HolePos[0]][self.HolePos[1]] == 1:
                            if self.solve():
                                return True
                        
                            #if there is no copy() here, the change of self.board in line 77-79 will
                            #   affect self.current.val. val in the node is a fixed array, not self.board. 
                            self.board = copy(parent.val)
                            parent.child, parent.jumpfrom, parent.jumpto = None, None, None
                            self.current = parent                                                        
        return False

startHoleRow, startHoleCol = np.inf, np.inf
while startHoleRow > 4:
    startHoleRow = int(raw_input("Please input row of the hole (<=4):"))
while startHoleCol > startHoleRow:
    startHoleCol = int(raw_input("Please input column of the hole (<=row):"))
    
game=board(startHoleRow, startHoleCol)
game.solve()
game.printSolution()
        
    